#!/usr/bin/env python
#-*- conding:utf-8 -*-

import twitter
import re
import time

#f = open("tweets.txt", "a")
wait = 90
while True:
    api = twitter.Api()
    satuses = api.GetPublicTimeline()
    print [s.user.name for s in statuses]
    time.sleep(wait)
