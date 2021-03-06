# -*- coding:utf-8 -*-
#!/usr/bin/python    

import HTML.Parser
import urlparse   
import urllib   
import urllib2   
import cookielib   
import string   
import re   
import json
import getpass


#从终端输入用户名和密码
user_name = raw_input("input username:\n")
password = getpass.getpass('password: ')

#登录的主页面   
hosturl = "https://i.kdslife.com/index.php"   
#post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据）   
posturl = 'https://passport.kdslife.com/index.php' 

#构造header，一般header至少要包含一下两项。这两项是从抓到的包里分析得出的。   
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',   
           'Referer' : '111'}   
#构造Post数据，他也是从抓大的包里分析得出的。   
postData = {'c' : 'login',  
            'm' : 'do_login',   
            'user_name' : user_name, 
            'password' : password
            } 	

class AutoLoginController(object):
     
    def __init__(self, hosturl, posturl, postData, headers):
        cj = cookielib.LWPCookieJar()   
        cookie_support = urllib2.HTTPCookieProcessor(cj)   
        opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)   
        urllib2.install_opener(opener) 
        
        h = urllib2.urlopen(hosturl)
        
        #需要给Post数据编码 
        postData = urllib.urlencode(postData)   
        #通过urllib2提供的request方法来向指定Url发送我们构造的数据，并完成登录过程   
        request = urllib2.Request(posturl, postData, headers)   
        #print "request",request  
        response = urllib2.urlopen(request)   
        text = response.read()
        #print text
        
        output = json.loads(text)
        print ("This is function call")
        print ("%15s%-35s"%('status: ', output['status']))
        print ("%15s%-35s"%('returned msg: ', output['msg']))
        print ("%15s%-35s"%('returned data: ', output['data']))

    def CookieInit(self):
        cj = cookielib.LWPCookieJar()   
        cookie_support = urllib2.HTTPCookieProcessor(cj)   
        opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)   
        urllib2.install_opener(opener) 

    def OpenHostUrl(self):
        urllib2.urlopen(hosturl)

KDSAutoLogin = AutoLoginController(hosturl,posturl, postData, headers)
KDSAutoLogin