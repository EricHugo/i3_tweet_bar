#!/usr/bin/env python

import tweepy
import sys

class retTwitter():
    def __init__(self, tokenfile):
        with open(tokenfile) as tf:
            tokens = [token.strip() for token in tf]
        auth = tweepy.OAuthHandler(tokens[0], tokens[1])
        auth.set_access_token(tokens[2], tokens[3])
        self.api = tweepy.API(auth)


    def retsearch(self, query):
        public_tweets = self.api.user_timeline(screen_name=query,
                                               count=1)
        for tweet in public_tweets:
            return tweet.text, tweet.user.name
        return tuple("No tweet found",)


if __name__ == "__main__":
    ret = retTwitter(sys.argv[1])
    tweet = ret.retsearch(sys.argv[2])
    print(tweet)

