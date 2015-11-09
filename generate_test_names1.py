import sys
import random
fh=open("test-name1.txt","w",encoding="utf-8")
for i in range(0,101):
	line = "{0}\n".format(random.choice(range(0,101)))
	fh.write(line)