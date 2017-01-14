import urllib2

req = urllib2.Request('https://www.github.com')
# req不可作为对象进行.read,但后续的urlopen可以简化
# you create a Request object that specifies the URL you want to fetch
response = urllib2.urlopen(req)
page = response.read()
#response是类似与文件的对象（file-like object）
#This response is a file-like object, which means you can for example call .read() on the response
print page
raw_input()
