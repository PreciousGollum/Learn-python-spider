import urllib2

req = urllib2.Request('https://www.github.com')
# req������Ϊ�������.read,��������urlopen���Լ�
# you create a Request object that specifies the URL you want to fetch
response = urllib2.urlopen(req)
page = response.read()
#response���������ļ��Ķ���file-like object��
#This response is a file-like object, which means you can for example call .read() on the response
print page
raw_input()
