# -*- coding:utf-8 -*-
'''
实例之糗事百科爬取
version 0.1
auther： Gollum
date:2017/1/17
refers to cuiqingcai.com/990.html
'''

import urllib
import urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
headers = { 'User-Agent' : user_agent }
try:
    req = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(req)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div.*? class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content".*?<span>(.*?)</span>.*?</a>(.*?)<div class="stats".*?number">(.*?)</i>', re.S)
    items = re.findall(pattern,content)
    for item in items:
        print 'author:'+ item[0] + '\n', 'text:'+ item[1] + '\n','votes:'+ item [3] +'\n'
    #item[0]:author, item[1]:contents, item[2]:imgs,  item[3] votes.
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
        
print 'End'
