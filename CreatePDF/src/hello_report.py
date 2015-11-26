from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
from reportlab.lib import colors

d=Drawing(1000,1000)
s=String(50,50,'Hello,World',textAnchor='middle')
d.add(s)
pl=PolyLine([(100,10),(20,11),(50,99)],strokeClor=colors.blue)
d.add(pl)
renderPDF.drawToFile(d, 'Hello.pdf', 'A simple PDF file') 
