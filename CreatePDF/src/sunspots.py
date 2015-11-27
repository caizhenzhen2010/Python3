#! urs/bin/env/python
#! -*- encoding: utf-8 -*-
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
from reportlab.lib import colors
from urllib import urlopen
from reportlab.graphics.charts.lineplots import LinePlot

#获得外部数据原型
url='http://services.swpc.noaa.gov/text/predicted-sunspot-radio-flux.txt'
COMMENT_CHARS="#:"
data=[]
for line in urlopen(url).readlines():
    if not line.isspace() and not line[0] in COMMENT_CHARS:
        #对外部数据原型改造
        data.append( [float(n) for n in line.split()])
prep=[row[2] for row in data]
high=[row[3] for row in data]
low =[row[4] for row in data]
times=[row[0]+row[1]/12.0 for row in data]
        
#创建Drawing
d=Drawing(400,200)
#创建LinePlot,并给予参数
lp=LinePlot()
lp.x=50
lp.y=50
lp.height=125
lp.width=300
lp.data=[zip(times,prep),zip(times,high),zip(times,low)]
lp.lines[0].strokeColor=colors.blue
lp.lines[1].strokeColor=colors.green
lp.lines[2].strokeColor=colors.red
#将LinePlot添加到Drawing
d.add(lp)
d.add(String(250,150,'Sunspots',fontsize=14,fillColor=colors.red))
#生成PDF文档
renderPDF.drawToFile(d, 'sunsport.pdf')
