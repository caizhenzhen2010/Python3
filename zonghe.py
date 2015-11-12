# -*- coding: utf-8 -*-
#---------------------------------------
#   程序：山东大学威海爬虫
#   版本：0.1
#   作者：sean
#   日期：2015-11-02
#   语言：Python 2.7
#   操作：输入学号和密码
#   功能：输出成绩的加权平均值也就是绩点
#---------------------------------------

import urllib  
import urllib2
#import cookielib

#cookie = cookielib.CookieJar()  
#opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

#需要GET的数据#
postdata=urllib.urlencode({  
    'userId':'201200620317',  
    'userPass':'6277977'  
})
user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers={'User-Agent':user_agent}
#自定义一个请求#
req = urllib2.Request(  
    url = 'http://202.194.40.15:8080/xsxt/xsxt.jsp',
    data = postdata,
	headers=headers
)

#访问该链接#
result = urllib2.urlopen(req)

#打印返回的内容#
filename='result.html'
#print result.read()   
f=open(filename,'wb')
f.write(result.read())
f.close()