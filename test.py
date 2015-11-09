#test 
import urllib2
import re
url='http://d.hiphotos.baidu.com/image/pic/item/48540923dd54564eb979a738b1de9c82d1584f96.jpg'
user_agent="Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
header={'User-Agent':user_agent}
req=urllib2.Request(url,headers=header)
result=urllib2.urlopen(req,timeout=10).read()
jpg_tuple=url.split('/')
jpg_filename=jpg_tuple[-1]
jpg=open(jpg_filename,'wb+')
jpg.write(result)
jpg.close()
