import configparser
import json

import twitter
import azure


class AirTweet(object):
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

    def analyze(self, query, max_items=1000):
        # Get tweets from Twitter
        tweets = self._twitter_api.search(query, max_items)

        # Compile tweets into Azure-formatted data
        docs = [{'id': k, 'text': v['text']} for k, v in tweets.items()]
        data = {'documents': docs}

        # Languages
        languages = self._azure_api.detect_language(data)
        for tweet in languages['documents']:
            language = tweet['detectedLanguages'][0]
            language = {
                'name': language['name'],
                'iso_6391': language['iso6391Name'],
                'score': language['score']
            }
            tweets[tweet['id']]['language'] = language

        # Sentiment
        sentiment = self._azure_api.sentiment(data)
        for tweet in sentiment['documents']:
            tweets[tweet['id']]['sentiment'] = tweet['score']

        # Key Phrases
        key_phrases = self._azure_api.key_phrases(data)
        for tweet in key_phrases['documents']:
            tweets[tweet['id']]['key_phrases'] = tweet['keyPhrases']

        return tweets
