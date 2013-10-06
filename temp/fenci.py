#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import json
# import jieba
import jieba.posseg as pseg
import csv
from utils import process_raw_tweet

# jieba.load_userdict('SougoDict.txt')

ws = {}

with open('wordset.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    reader.next()
    for row in reader:
        ws[row[0]] = int(row[6])


def detect_polarity(content):
    # 带词性分词
    words = pseg.cut(content)
    # 去除数量词和无意义词
    denoised = filter(lambda x: x.flag not in ('x', 'm'), words)
    p, n = 0, 0
    for x in denoised:
        try:
            e = ws[x.word.encode('utf-8')]  # 这是一个坑
        except KeyError:
            continue
        if e == 1:
            p += 1
        elif e == 2:
            n += 1
        else:
            continue
    if p == n:
        return u'中性'
    elif p > n:
        return u'正向'
    else:
        return u'负向'


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
        p = detect_polarity(content)
        print i, p, raw_content
        #print i, content
        #print i, '|'.join(jieba.cut(content))

        #print i, ' '.join([x.word for x in denoised])
    f.close()

# vim: sw=4 ts=4 sts=4 expandtab
