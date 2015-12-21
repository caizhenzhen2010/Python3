#! /usr/bin/env python
#coding=utf-8
#统计行数
def countline(f):
    count=0
    with open(f,'r') as myfile:
        for line in myfile:
            count+=1
    return count

print countline('text.txt')