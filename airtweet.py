import configparser
import json

import twitter
import azure


_DEFAULT_CONFIG_PATH = 'airtweet.ini'


def _read_config_file(config_path):
    config = configparser.ConfigParser()
    config.read(config_path)
    return config


class AirTweet(object):
    def __init__(self, config_path=None):
        config_path = config_path or _DEFAULT_CONFIG_PATH
        config = _read_config_file(config_path)

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
        import pprint
        pprint.pprint(data)

        # Sentiment
        sentiment = self._azure_api.sentiment(data)
        for tweet in sentiment['documents']:
            tweets[tweet['id']]['sentiment'] = tweet['score']

        # Key Phrases
        key_phrases = self._azure_api.key_phrases(data)
        for tweet in key_phrases['documents']:
            tweets[tweet['id']]['key_phrases'] = tweet['keyPhrases']

        return tweets
