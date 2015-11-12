import sys
x=["Sloop","Yawl","Cutter","schooner","ketch"]
temp=[]
for item in x:
	temp.append((item.lower()))
x=[]
for value in sorted(temp):
	x.append(value)
for i in x:
	print("{0}".format(i))