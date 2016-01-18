#! /usr/bin/python2.7
#! encoding:utf-8
import os
import sys

def myfun(n,filename):
    myfile=open(filename,'rb')
for line in myfile.readline():
    mystr=line.split(' ')
    relist=zip(*[mystr[i] for i in range(n)])
    
myfile.close()       
if __name__=='__main__':
    myfun(sys.argv[1],sys.argv[2])