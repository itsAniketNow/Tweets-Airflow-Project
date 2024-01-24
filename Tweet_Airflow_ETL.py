import tweepy
import pandas as pandas
import json
from datetime import datetime
import s3fs


access_key = "RVXrXA9QjC9UEhOB2wbO0bdhJ"
access_secret = "UNz5drjBdwFunFMI7PDNMjgK91ubVO1o5rc6wBaRFBeF1I3oSb"
consumer_key = "1749696713164554240-omYJVdS9SxDicXxxheG0gdTZ8RhAP0"
consumer_secret = "IMCozChroLas4NKogIQARjDaTzn0AP4N3DcGaf8R0889T"

# Tweeter Authentication
auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key, consumer_secret)

# Create the APi Object
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name = "@elonmusk",
                           # 200 is the maximum allowed account
                           count = 200,
                           include_rts = False,
                           # Necessary to keep full_text
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended')

tweet_list = []
for tweet in tweets:
    text = tweet._json['full_text']
    
    refined_tweet = { 'user' : tweet.user.screen_name,
                     'text' : text,
                     'favorite_count' : tweet.fevorite_count,
                     'retweet_count' : tweet.retweet_count,
                     'created_at' : tweet.created_at}
    
    
    tweet_list.append(refined_tweet)
    
    
    df = pd.DataFrame(tweet_list)
    df.to_csv('refined_tweets.csv')