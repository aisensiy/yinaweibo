#!/usr/bin/env python
# encoding: utf-8


import re
from datetime import datetime
from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from yinaweibo.items import WeiboItem

cookies = """You Cookies Here"""


class WbSpider(Spider):
    name = "wbspider"
    allowed_domains = ["weibo.com"]

    def __init__(self, filepath=None, *args, **kvargs):
        super(WbSpider, self).__init__(*args, **kvargs)
        # self.urls = ['http://weibo.cn/3985732098']
        self.urls = [d.strip() for d in open(filepath)]
        # set cookies
        rawcookie = cookies
        self.cookies = dict([pair.split('=', 1)
                             for pair in rawcookie.split('; ')])
        self.log('urls: %d' % len(self.urls))

    def start_requests(self):
        return [Request(url=url, cookies=self.cookies) for url in self.urls]

    def parse(self, response):
        sel = Selector(response)
        weibo_elems = sel.css('div.c[id^="M_"]')
        uid = re.search('weibo\.cn\/u\/(\d+)', response.url).group(1)

        weibos = []
        for elem in weibo_elems:
            weibo = WeiboItem()
            weibo['uid'] = uid
            div = elem.css(u'div:contains(转发理由):not([id])')
            if len(div) != 0:
                weibo['repostcontent'] = elem.css('span.ctt').extract()[0]
                weibo['content'] = div.extract()[0]
            else:
                weibo['content'] = elem.css('span.ctt').extract()[0]

            weibo['weiboid'] = elem.css('::attr(id)').re('M_(.+)')[0]
            weibo['zancount'] = elem.css(u'div a:contains(赞)::text').re('\d+')[0]
            weibo['repostcount'] = elem.css(u'div a:contains(转发)::text').re('\d+')[0]
            weibo['commentcount'] = elem.css(u'div a:contains(评论)::text').re('\d+')[0]
            weibo['currenttime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            weibo['time'] = elem.css('span.ct::text').extract()[0]
            weibos.append(weibo)

        return weibos
