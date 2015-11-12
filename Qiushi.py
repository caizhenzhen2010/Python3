# -*- coding: utf-8 -*-
#---------------------------------------
#   程序：糗事百科
#   版本：0.1
#   作者：sean
#   日期：2015-11-02
#   语言：Python 2.7
#   操作：
#   功能：获得糗事百科图片
#---------------------------------------
import urllib
import urllib2
import re
import sys

class Qiushi:
#头信息设置
	def __init__(self,maxpage_index):
		self.maxpage_index=maxpage_index
		self.user_agent="Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
		self.header={'User-Agent':self.user_agent}
	def start(self):
		
		url="http://www.qiushibaike.com/pic/page/"
		myItems=list()
		for index in range(1,self.maxpage_index):
			url="http://www.qiushibaike.com/pic/page/"
			url+=str(index)
			req=urllib2.Request(url,headers=self.header)
			result=urllib2.urlopen(req).read()
			myPage=result.decode('utf-8')
			self.saveFile(filename="myPage.html",myPage=myPage)
			myItem = re.findall('<div class="thumb">(.*?)<img src="(.*?)" alt=(.*?) />',myPage,re.S)
			myItems.append(myItem)
		return myItems
		
	def saveImage(self,myItems):
		#保存图片
		for myItem in myItems:
			for item_jpg in myItem:
				#self.saveFile(filename='myItem.txt',myPage=item_jpg[1])
				req=urllib2.Request(url=item_jpg[1],headers=self.header)
				result=urllib2.urlopen(req).read()
				jpg_tuple=item_jpg[1].split('/')
				jpg_filename=jpg_tuple[-1]
				jpg=open(jpg_filename,'wb+')
				jpg.write(result)
				jpg.close()
				
	def saveFile(self,filename,myPage):
		f=open(filename,'a')
		f.write(myPage)
		f.close()
			
reload(sys)
sys.setdefaultencoding( "utf-8" )
qiushi=Qiushi(10)
myItems=qiushi.start()
qiushi.saveImage(myItems)