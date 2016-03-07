#!/usr/bin/python

import os
import urllib2
import cookielib

'''
response = urllib2.urlopen('http://www.baidu.com')

print response.getcode()
cont = response.read()
'''


url = 'http://www.baidu.com'
request = urllib2.Request(url)

request.add_header('User-Agent', 'Mozilla/5.0')

response = urllib2.urlopen(request)
print response.getcode()
cont = response.read()

'''
url = "http://www.baid.com"
cj = cookielib.CookieJar()

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

response = urllib2.urlopen(url)
print response.getcode()
cont = response.read()
'''

try:
    f = os.open('index.html',os.O_CREAT | os.O_RDWR)
    os.write(f, cont)
except:
    print "file open error"
finally:
    try:
        os.close(f)
        print "over"
    except:
        print "NameError"
