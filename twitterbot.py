import tweepy
from time import sleep

consumer_key = 'XXXXXXXXXX'
consumer_secret = 'XXXXXXXXXX'
access_token = 'XXXXXXXXXX'
access_token_secret = 'XXXXXXXXXX'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q='#example').items(5):
    try:
        tweet.retweet()
        print('Retweet published successfully.')
        sleep(10)

    except tweepy.TweepError as error:
        print(error.reason)

    except StopIteration:
        break
