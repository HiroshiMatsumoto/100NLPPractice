#! /usr/bin/env python
# -*- encode: utf-8 -*-

#Ref: http://code.google.com/p/python-twitter/
import twitter

api = twitter.Api()
status = api.GetPublicTimeline()
print [s.text for s in status]
