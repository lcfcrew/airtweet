import requests
import json


class AzureAPI(object):
    """
    A wrapper for the Azure Cognitive Services Text Analysis APIs. Automatically
    deserializes the JSON response data and returns the body as a dictionary.
    """

    _API_URI = 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/'

    def __init__(self, subscription_key):
        self._headers = {
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': subscription_key
        }

    def detect_language(self, data):
        """
        Detects the primary languages of documents in ``data``.

        :param data:
        :return:
        """
        return self._post('languages', data)

    def detect_topics(self):
        """
        Detects topics among documents in ``data``.

        :param data:
        :return:
        """
        raise NotImplementedError()

    def key_phrases(self, data):
        """
        Detects key phrases of each document in ``data``.

        :param data:
        :return:
        """
        return self._post('keyPhrases', data)

    def sentiment(self, data):
        """
        Detects overall sentiment of each document in ``data``.

        :param data:
        :return:
        """
        return self._post('sentiment', data)

    def _post(self, service, data):
        uri = self._API_URI + service
        response = requests.post(uri, json=data, headers=self._headers)
        return json.loads(response.text)
