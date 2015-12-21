#! /usr/bin/env python
#coding=utf-8

if __name__=='__main__':
    print '程序运行，初始化'
elif __name__=='mtest':
    print '被import'

score=400
if(score>=90) and (score<=100):  
    print "A"  
elif(score>=80 and score<90):  
    print "B"  
elif(score>=60 and score<80):  
    print "C"  
else:  
    print "D"  