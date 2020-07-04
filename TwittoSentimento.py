# TwittoSentimento.py
import tweepy
from textblob import TextBlob

consumer_key = '1AUDHrUbI2EOs3lmIJCiNvD0Q'
consumer_secret = 'Jah2rEJLbfhIl8JvipLXYxxGgafusRUbB35MX7NcqfeY0I196H'

access_token = '1278008765841719297-vGBvbsLXWrGJ5pucODxkVD9iitETnZ'
access_token_secret = 'rZTgq1XI0XbREUspIDiutARIgURFnwHVIuOChaS6apIhU'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# tweepy.API(): This class provides a wrapper for the API as provided by Twitter.
# we can create tweets, delete tweets and find twitter users
api = tweepy.API(auth)

public_tweets= api.search('#sikh')

for tweet in public_tweets:
    #print (tweet.text)
    # TextBlob() accepts only text argument
    analysis = TextBlob(tweet.text)
    #print(analysis.sentiment)
    x = analysis.sentiment.polarity
    if x > 0:
        positive_polarity_tweets = open('D:\Python\Atom Files\TwittoPoitiveSentimento.txt', 'w')
        positive_polarity_tweets.write(tweet.text)
        positive_polarity_tweets.close()

    elif x < 0:
            negative_polarity_tweets = open('D:\Python\Atom Files\TwittoNegativeSentimento.txt', 'w')
            negative_polarity_tweets.write(tweet.text)
            negative_polarity_tweets.close()
