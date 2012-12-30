# -*- coding: utf-8 -*-
import twitter
import re
import time

f = open("tweets.txt", "a")
wait = 90
while True:
    api = twitter.Api()
    for s in api.GetPublicTimeline():
        f.write((s.text+"\n").encode("utf-8"))
        #if re.search(u"[ぁ-ゞ]", s.text):
        #    f.write((s.text+"\n").encode("utf-8"))
    time.sleep(wait)

