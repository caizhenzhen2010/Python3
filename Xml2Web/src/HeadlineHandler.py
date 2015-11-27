#! /usr/bin/env python
#! -*- encoding: utf-8 -*-

from xml.sax.handler import ContentHandler
from xml.sax import parse

class HeadlineHandler(ContentHandler):
    is_header=False
    def __init__(self,headlines):
        ContentHandler.__init__(self)
        self.headlines=headlines
        self.data=[]
        
    def startElement(self, name, attrs):
        if name=='h1':
            self.is_header=True
    def endElement(self, name):
        if name=='h1':
            text=''.join(self.data)
            self.headlines.append(text)
            self.data=[]
            self.is_header=False
    def characters(self, content):
        if self.is_header==True:
            self.data.append(content)
            
headlines=[]
parse('website.xml', HeadlineHandler(headlines))
print 'The following <h1> elemnets were founnd!'
for header in headlines:
    print header
