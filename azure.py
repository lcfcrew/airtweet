import requests
import json


class AzureAPI(object):
    _API_URI = 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/'

    def __init__(self, subscription_key):
        self._headers = {
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': subscription_key
        }

    def detect_language(self):
        raise NotImplementedError()

    def detect_topics(self):
        raise NotImplementedError()

    def key_phrases(self, data):
        return self._post('keyPhrases', data)

    def sentiment(self, data):
        return self._post('sentiment', data)

    def _post(self, service, data):
        uri = self._API_URI + service
        response = requests.post(uri, json=data, headers=self._headers)
        return json.loads(response.text)
