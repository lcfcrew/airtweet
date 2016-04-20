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
        data = {'documents': []}
        for key, value in tweets.items():
            data['documents'].append({
                'id': key,
                'text': value['text']
            })

        # Detect sentiment
        sentiment = self._azure_api.sentiment(data)
        for tweet in sentiment['documents']:
            tweets[tweet['id']]['sentiment'] = tweet['score']

        return tweets
