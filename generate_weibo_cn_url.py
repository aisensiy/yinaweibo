#!/usr/bin/env python
# encoding: utf-8


def generate_urls(uid, statuscount, perpage=10):
    if statuscount % perpage == 0:
        pagecount = statuscount / perpage
    else:
        pagecount = statuscount / perpage + 1

    return ['http://weibo.cn/u/%d?page=%d&st=ee25' % (uid, page)
            for page in xrange(1, pagecount + 1, 5)]


if __name__ == '__main__':
    import pandas as pd
    import sys
    df = pd.read_csv(sys.argv[1])
    urls = []

    for idx, row in df.iterrows():
        urls += generate_urls(row['uid'], row['weibocount'])

    with open(sys.argv[2], 'w') as ofile:
        for url in urls:
            ofile.write(url + '\n')
