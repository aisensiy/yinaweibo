# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class WeiboItem(Item):
    uid = Field()
    weiboid = Field()
    content = Field()
    zancount = Field()
    repostcount = Field()
    commentcount = Field()
    currenttime = Field()
    time = Field()
    repostcontent = Field()
