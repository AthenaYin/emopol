#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import re

rx_tcn = re.compile(r'http:\/\/t\.cn\/[A-Za-z0-9]*')
rx_retweet = re.compile(r'\/\/@[^:]+:')
rx_username = re.compile(r'@[^\s:]+')


def process_raw_tweet(raw_content, user=None):
    content = rx_tcn.sub('', raw_content)
    tweets = rx_retweet.split(content)
    tweets = map(lambda x: rx_username.sub('', x), tweets)
    #?
    tweets = map(lambda x: x.strip(), tweets)
    # print i, '|'.join(tweets)

    tweet = tweets[0]
    #?
    if user is not None:
        rx_user = r'^' + user + u'：'
        tweet = re.sub(rx_user, '', tweet)
        tweet = re.sub(u'^回复:', '', tweet)
    return tweet

# vim: ts=4 sw=4 sts=4 expandtab
