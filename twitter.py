import tweepy


class TwitterAPI(object):
    """
    A wrapper for the Twitter API which automatically authenticates and
    serializes search results.
    """

    def __init__(self, consumer_token, consumer_secret, access_token,
                 access_secret):
        auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        self._api = tweepy.API(auth)

    def search(self, query, max_items=1000):
        """
        Searches Twitter for tweets matching the given query. Results are
        placed in a dictionary using the tweet id as the key.

        :param query: A search string
        :param max_items: The maximum number of tweets to return
        :return: A dictionary of tweets (by "id")
        """
        cursor = tweepy.Cursor(self._api.search, q=query).items(max_items)
        tweets = {}
        for tweet in cursor:
            tweets[str(tweet.id)] = {'text': tweet.text}
        return tweets
