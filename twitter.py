import tweepy


class TwitterAPI(object):
    def __init__(self, config):
        auth = tweepy.OAuthHandler(
            config['CONSUMER_TOKEN'],
            config['CONSUMER_SECRET']
        )
        auth.set_access_token(
            config['ACCESS_TOKEN'],
            config['ACCESS_SECRET']
        )
        self._api = tweepy.API(auth)

    def search(self, query, max_items=1000):
        cursor = tweepy.Cursor(self._api.search, q=query).items(max_items)
        tweets = {}
        for tweet in cursor:
            tweets[str(tweet.id)] = {'text': tweet.text}
        return tweets
