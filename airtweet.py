import configparser
import json

import twitter
import azure


class AirTweet(object):
    """
    An interface to analyze Twitter search results using the Azure Cognitive
    Services Text Analysis API.

    **NOTE:** Requires an `airtweet.ini` file with Twitter API tokens and
    an Azure subscription key.
    """

    def __init__(self, config_path='airtweet.ini'):
        config = configparser.ConfigParser()
        config.read(config_path)

        # Twitter API
        twitter_config = config['TwitterAPI']
        self._twitter_api = twitter.TwitterAPI(
            twitter_config['CONSUMER_TOKEN'], twitter_config['CONSUMER_SECRET'],
            twitter_config['ACCESS_TOKEN'], twitter_config['ACCESS_SECRET'])

        # Azure API
        azure_config = config['AzureAPI']
        self._azure_api = azure.AzureAPI(
            azure_config['SUBSCRIPTION_KEY'])

    def analyze(self, query, max_items=1000, do_language_detection=True,
                do_sentiment_analysis=True, do_key_phrase_detection=True):
        """
        Analyzes Twitter search results using Azure Cognitive Services Text
        Analysis APIs.

        :param query: A string query
        :param max_items: The maximum number of tweets to fetch
        :param do_language_detection: Perform language detection
        :param do_sentiment_analysis: Perform sentiment analysis
        :param do_key_phrase_detection: Perform key phrase detection
        :return: A dictionary of analyzed tweets
        """
        # Get tweets from Twitter
        tweets = self._twitter_api.search(query, max_items)

        # Compile tweets into Azure-formatted data
        docs = [{'id': k, 'text': v['text']} for k, v in tweets.items()]
        data = {'documents': docs}

        if do_language_detection:
            languages = self._azure_api.detect_language(data)
            for tweet in languages['documents']:
                language = tweet['detectedLanguages'][0]
                language = {
                    'name': language['name'],
                    'iso_6391': language['iso6391Name'],
                    'score': language['score']
                }
                tweets[tweet['id']]['language'] = language

        if do_sentiment_analysis:
            sentiment = self._azure_api.sentiment(data)
            for tweet in sentiment['documents']:
                tweets[tweet['id']]['sentiment'] = tweet['score']

        if do_key_phrase_detection:
            key_phrases = self._azure_api.key_phrases(data)
            for tweet in key_phrases['documents']:
                tweets[tweet['id']]['key_phrases'] = tweet['keyPhrases']

        return tweets
