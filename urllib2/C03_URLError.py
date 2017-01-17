import urllib2

req = urllib2.Request('https://www.github.com/why.html')
try:
    response = urllib2.urlopen(req)
except urllib2.URLError, e:
    if hasattr(e, 'reason'):
        print 'Reason:',e.reason
    elif hasattr(e,'code'):
        print 'code:'.e.code
#URLError一般给出一个带有reason属性的描述，包含一个错误代码（error code）和文本错误信息（text error message）
#HTTPError为服务器HTTP响应是的数字状态码（status code）如404，503
#URLError为HTTPError的一个子类
else:
    #everything is fine
    print 'fine'
raw_input()
