import tweepy


class TwitterAPI(object):
    def __init__(self, consumer_token, consumer_secret, access_token,
                 access_secret):
        auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        self._api = tweepy.API(auth)

    def search(self, query, max_items=1000):
        cursor = tweepy.Cursor(self._api.search, q=query).items(max_items)
        tweets = {}
        for tweet in cursor:
            tweets[str(tweet.id)] = {'text': tweet.text}
        return tweets
