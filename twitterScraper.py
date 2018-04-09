#!/usr/bin/env python

from tweepy import OAuthHandler
import tweepy
import json
from time import sleep
import sys

# Keys provided from the Twitter custom application
consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
#---------------------

# Where On Earth ID - WOEID 
# (http://www.woeidlookup.com/)
# 1       - Worldwide
# 2459115 - NYC
# 2367105 - Suffolk County (Boston)
WOEID = 2459115

# Get trending topics for a specific WOEID
# TODO: Get trending topics every 5 min
trends1 = api.trends_place(WOEID)
trends1
trends = set([trend['name'] for trend in trends1[0]['trends']])
trendsList = list(trends)

with open("favorites.txt", 'a') as f:
	if (WOEID == 2459115):
		f.write('Trending topics in NYC: \n')
	elif (WOEID == 2367105):
		f.write('Trending topics in BOS: \n')
	else:
		print 'WOEID not supported!'

	# From trending topics, get Tweets
	for t in trendsList:
		print 'Retrieving tweets for ' + str(t)
		sys.stdout.flush()
		for tweet in tweepy.Cursor(api.search, q=t, rpp=100, since="2018-03-14", lang="en").items(1000):
			f.write(json.dumps([tweet._json], indent=1))
			f.write('\n')
			sleep(0.5)
