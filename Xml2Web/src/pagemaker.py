#! /urs/bin/env/Python
#! -*- encoding: utf-8 -*-

from xml.sax.handler import ContentHandler
from xml.sax import parse

class pagemaker(ContentHandler):
    is_through=False
    def startElement(self, name, attrs):
        if name=='page':
            self.is_through=True
            self.out=open(attrs['name']+'.html','w')
            self.out.write('<html>\n')
            self.out.write('<head>\n')
            self.out.write('<title>')
            self.out.write(attrs['title'])
            self.out.write('\n')
            self.out.write('</title>\n')
            self.out.write('</head>\n')
            self.out.write('<body>\n')
        elif self.is_through:
            self.out.write('<'+name)
            for key,value in attrs.items():
                self.out.write(' %s=%s'%(key,value))
            self.out.write('>')
    def endElement(self, name):
        if name=='page':
            self.is_through=False
            self.out.write('</body>\n</html>')
            self.out.close()
        elif self.is_through:
            self.out.write('</%s>'%name)
    def characters(self, content):
        if self.is_through:
            self.out.write(content)
            
parse('website.xml', pagemaker())