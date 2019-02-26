#!/usr/bin/env python

from __future__ import print_function
import sys
import re
import os
from time import strftime, localtime, sleep
from rettwitter import retTwitter

PATH = os.path.realpath(__file__)
TOKENFILE = PATH + '/../share/tokens.list'
RET = retTwitter(TOKENFILE)
ILLEGAL_CHARS = "\""

def get_clock():
    return strftime("%a, %d %b %Y %H:%M:%S", localtime())

def format_tweet(query):
    tweet = RET.retsearch(query)
    return tweet

def main():
    print('{ "version": 1 }')
    print('[')
    print('[]')
    i = 60
    while True:
        if i >= 60:
            try:
                tweet = format_tweet("genomeresearch")
            except Exception:
                tweet = ("Error:", "there is an issue with the tweet fetching"\
                                    "at the moment")
            i = 0
        print(",[{\"name\":\"divider\",\"full_text\":\"@%s: %s \",\"color\":"\
              "\"#FFFFFF\"}" % (tweet[1], re.sub(re.escape(ILLEGAL_CHARS), '', tweet[0])))
        print(",{\"name\":\"time\",\"full_text\":\" %s \",\"color\":"\
              "\"#57c7ff\"}" % get_clock())
        print(",{\"name\":\"divider_end\",\"full_text\":\" \",\"color\":"\
              "\"#FFFFFF\"}]")
        sys.stdout.flush()
        i += 1
        sleep(1)
    # get time
    # get tweet

if __name__ == "__main__":
    main()
