# Scrapy settings for yinaweibo project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'yinaweibo'

SPIDER_MODULES = ['yinaweibo.spiders']
NEWSPIDER_MODULE = 'yinaweibo.spiders'
DOWNLOAD_DELAY = 1

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'yinaweibo (+http://www.yourdomain.com)'
