import urllib2

req = urllib2.Request('https://www.douyu.com/98653558')
try:
    response = urllib2.urlopen(req)
except urllib2.URLError, e:
    if hasattr(e, 'reason'):
        print 'Reason:',e.reason
    elif hasattr(e,'code'):
        print 'code:'.e.code
#URLErrorһ�����һ������reason���Ե�����������һ��������루error code�����ı�������Ϣ��text error message��
#HTTPErrorΪ������HTTP��Ӧ�ǵ�����״̬�루status code����404��503
#URLErrorΪHTTPError��һ������
else:
    #everything is fine
    print 'fine'
raw_input()
