import urllib, urllib2

webopener = urllib2.build_opener()
#新建一个opener
auth = urllib2.HTTPBasicAuthHandler()
#新建一个认证handler
webopener.addheaders = [('User-agent', 'Mozilla/5.0')]
auth.add_password('Admin','http://www.dygod.net','Gollum','password')
#h.add_password('realm','url','user','password')
response = webopener.open('http://www.dygod.net')
#用新建的opener打开网址
page = response.read()
print page
raw_input()
