#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import json
import jieba
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


if __name__ == "__main__":

    f = open('sample.txt')
    for i, line in enumerate(f):
        text = line.strip()
        if not text:
            continue

        try:
            weibo = json.loads(text)
        except Exception, e:
            continue

        raw_content = weibo['mt']
        username = weibo['sn']
        content = process_raw_tweet(raw_content, username)
        #print i, content
        print i, '|'.join(jieba.cut(content))

    f.close()

# vim: sw=4 ts=4 sts=4 expandtab
