# -*- coding: utf-8 -*-
import urllib
import urllib2
import re


f = open('D://Qingqing.doc','w')
pn = 0
def_url = 'http://tieba.baidu.com/p/1571646862?'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
headers = {"User_agent":user_agent}
url = def_url + 'pn=' + str(pn)
req = urllib2.Request(url, headers = headers)
response = urllib2.urlopen(req)
page = response.read().decode('utf-8')
counter = re.findall(re.compile('<span class="red">(.*?)</span>',re.S),page)
print counter
for item in counter:
    t = item
while pn <= int(t):
    pn = pn + 1
    url = def_url + 'pn=' + str(pn)
    print '正在写入第',pn,'页'
    req = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(req)
    page = response.read().decode('utf-8')
    pattern = re.compile(r'<div class="louzhubiaoshi_wrap">.*?<div id="post_content.*?>(.*?)</div>',re.S)
    items = re.findall(pattern, page)
    for item in items:
        item = re.sub(re.compile('<a.*?>|</a>'),"",item)
        item = re.sub(re.compile('<br.*?>|</br>'),"",item)
        f.write(item.encode('gbk'))
print 'Enter to end'
f.close()
raw_input()
