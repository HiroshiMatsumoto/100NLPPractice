#! /usr/bin/env python
# -*- encode: utf-8 -*-
#ref: http://packages.python.org/tweepy/html/getting_started.html
import tweepy

public_tweets = tweepy.api.public_timeline()

for tweets in public_tweets:
    print tweet.text
