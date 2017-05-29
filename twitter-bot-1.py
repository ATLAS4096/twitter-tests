#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# This bot listens to a feed on a refresh timer and prints recent tweets.
#

import time
import tweepy
from credentials import *

# Initialize and authenticate
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Global variables
targetFeed = '<SOMEUSER>'
mostRecentTweetOnFeed = None
tweettext = 'Testing 123'

def readEvalTweet():

    global mostRecentTweetOnFeed

    # Get the latest tweet from target feed
    timeline = api.user_timeline(targetFeed)
    for tweet in timeline:
        print(tweet.text)
        print(tweet.id)

    # See if it is newer than last, if so, tweet
    # if checkedTweet != mostRecentTweetOnFeed:
    #     ###api.update_status(status=tweettext)
    #     print('Would Tweet: ' + tweettext)

    # mostRecentTweetOnFeed = checkedTweet

# Here is the refresh loop for the bot

while True:
    refreshRate = 15
    readEvalTweet()
    print('Refreshing feed in ' + str(refreshRate) + ' seconds.')
    time.sleep(refreshRate)

