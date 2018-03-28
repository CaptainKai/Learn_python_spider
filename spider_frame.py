# -*- coding: utf-8 -*-
# python27
import urllib2
from bs4 import BeautifulSoup
import re
'''structured code from imooc_spider.py'''
def UrlManager():
    root_url = 'https://baike.baidu.com/item/Python/407313'
    return root_url
def UrlDownloader(url):
	respence = urllib2.urlopen(url)
	return respence.read().decode('utf-8')
def UrlParser(data):
    soup = BeautifulSoup()
def main():
    url = UrlManager()
    # new_urls, new_data = UrlDownloader(url)

if __name__ == '__main__':
    main()