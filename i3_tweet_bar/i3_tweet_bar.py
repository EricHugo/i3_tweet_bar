#!/usr/bin/env python

from __future__ import print_function
import sys
import re
import os
from time import strftime, localtime, sleep
from rettwitter import retTwitter

PATH = '/'.join(os.path.realpath(__file__).split('/')[:-1])
TOKENFILE = PATH + '/../share/tokens.list'
RET = retTwitter(TOKENFILE)
ILLEGAL_CHARS = "[\"\']"

def get_clock():
    return strftime("%a, %d %b %Y %H:%M:%S", localtime())

def format_tweet(query=None):
    tweet = RET.retsearch(query)
    split_tweet = tweet[0].split('\n')
    test = ' '.join(split_tweet)
    formatted_tweet = [test] + [tweet[1]]
    return formatted_tweet

def main():
    print('{ "version": 1 }')
    print('[')
    print('[]')
    i = 60
    while True:
        if i >= 60:
            try:
                tweet = format_tweet()
            except Exception as e:
                tweet = ("there is an issue with the tweet fetching "\
                                    "at the moment", "Error")
            i = 0
        print(",[{\"name\":\"tweet\",\"full_text\":\"@%s: %s \",\"color\":"\
              "\"#FFFFFF\"}" % (tweet[1], re.sub(ILLEGAL_CHARS, '', tweet[0])))
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
