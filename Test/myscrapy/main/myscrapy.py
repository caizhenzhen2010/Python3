#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Create on 2016年1月18日
@author: sean
'''

import Queue
import urllib2
import re

class my_scrapy():
    """
    自己的爬虫程序 类my_scrapy
    """
    def __init__(self,url):
        """
        初始化函数
        """
        self.url_queue=Queue.Queue()
        self.url_set=set()
        self.url_set.add(url)
        self.url_queue.put(url)

    def process(self):
        """
        处理主程序
        """
        while (True):
            if self.url_queue.qsize()>0:
                current_url=self.url_queue.get()
                print current_url
                for next_url in self.get_next(current_url):
                    if next_url not in self.url_set:
                        self.url_set.add(next_url)
                        self.url_queue.put(next_url)
            else:
                 break
    
    def store(self,url,url_content):
        """
        存储网页
        """
        try:
            store_file=open(url.split('/')[-1]+'.html','wb+')
            store_file.write(url_content)
            store_file.flush()
            store_file.close()
            print '成功存储html文件:'.join(url.split('/')[-1].join('.html'))
        except Exception,e:
            print e
            
    def get_next(self,url):
        """
        从网页中提取url
        """
        try:
            url_content=self.get_content(url)
            self.store(url, url_content)
            ss=url_content.replace(' ','')
            urls=re.findall(r"<a.*?href=\"http(.*?)\"",ss,re.I)
            for url in urls:
                yield 'http'.join(url.strip('/'))
        except Exception,e:
            print e
            
    def get_content(self,url):
        """
        读取网页内容
        """
        try:
            url_content=urllib2.urlopen(url,timeout=5).read()
        except Exception,e:
            print e
        else:
            return url_content
    
    