import requests


class AzureAPI(object):
    _API_URI = 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/'

    def __init__(self, config):
        self._subscription_key = config['SUBSCRIPTION_KEY']

    def detect_language(self):
        raise NotImplementedError()

    def detect_topics(self):
        raise NotImplementedError()

    def key_phrases(self):
        raise NotImplementedError()

    def sentiment(self, data):
        return requests.post(self._API_URI + 'sentiment', data)
