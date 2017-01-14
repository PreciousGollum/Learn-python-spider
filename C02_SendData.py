# -*- coding: cp936 -*-
import urllib
import urllib2

data = {}
data['name']  = 'yourname'
data['password'] = 'password'
values = urllib.urlencode(data)
#print values
user_agent = 'Mozila/4.0'
#Users Agent header
url = 'http://www.github.com'
full_url = url + '?' + values
#GET方式，构建带参数的URL
#full URL is created by adding a ? to the URL, followed by the encoded values.
data = urllib2.urlopen(full_url)
page = data.read()
print full_url
print page
raw_input()
