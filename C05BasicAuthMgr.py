import urllib2

pagede = urllib2.urlopen('https://www.github.com').read()
#��֤ǰ��ȡ��Ϣ
passwd_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
passwd_mgr.add_password('None','http://www.github.com','users','password')
#�����������
handler = urllib2.HTTPBasicAuthHandler(passwd_mgr)
opener = urllib2.build_opener(handler)
deurl = 'http://www.github.com'
opener.open(deurl)
urllib2.install_opener(opener)

response = urllib2.urlopen(deurl)
page = response.read()
print page
print '------------------------------------------------------------'
'---------------------------------------------------------'
print pagede
raw_input()
