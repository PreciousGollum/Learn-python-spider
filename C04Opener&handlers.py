import urllib, urllib2

webopener = urllib2.build_opener()
#�½�һ��opener
auth = urllib2.HTTPBasicAuthHandler()
#�½�һ����֤handler
webopener.addheaders = [('User-agent', 'Mozilla/5.0')]
auth.add_password('Admin','http://www.dygod.net','Gollum','password')
#h.add_password('realm','url','user','password')
response = webopener.open('http://www.dygod.net')
#���½���opener����ַ
page = response.read()
print page
raw_input()
