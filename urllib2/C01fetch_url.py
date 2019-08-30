import urllib.request
# urllib2 had been remove from python3,import urllib.request instead import import urllib2

response = urllib.request.urlopen('https://www.github.com')
# you create a Request object that specifies the URL you want to fetch

page = response.read()
#response���������ļ��Ķ���file-like object��
#This response is a file-like object, which means you can for example call .read() on the response
print (page)
