import sys
if len(sys.argv)<3:
	print("usage:grepword.py word infile1 [infiles2 [...infileN]]")
	sys.exit()
word = sys.argv[1]
for filename in sys.argv[2:]:
	for lino,line in enumerate(open(filename),start=0):
		if word in line:
			print("{0}:{1}:{2:40}".format(filename,lino,line.rstrip()))
			