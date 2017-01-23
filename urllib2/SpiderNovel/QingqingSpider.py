import urllib
import urllib2
import re


url = 'http://tieba.baidu.com/p/1571646862?' 
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
headers = {"User_agent":user_agent}
req = urllib2.Request(url, headers = headers)
response = urllib2.urlopen(req)
page = response.read().decode('utf-8')
pattern = re.compile(r'<div class="louzhubiaoshi_wrap">.*?<div id="post_content.*?>(.*?)</div>',re.S)
items = re.findall(pattern, page)
contents = []
for item in items:
    item = re.sub(re.compile('<a.*?>|</a>'),"",item)
    item = re.sub(re.compile('<br.*?>|</br>'),"",item)
    print item
print 'enter to end'

raw_input()
