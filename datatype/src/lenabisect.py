#! /usr/bin/env python
#coding=utf-8
import bisect
import random
   
# Use aconstant seed to ensure that
# the samepseudo-random numbers
# are usedeach time the loop is run.
random.seed(1)
   
print'New  Pos Contents'
print'---  --- --------'
   
# Generaterandom numbers and
# insert theminto a list in sorted
# order.
l = []
for i in range(1, 15):
#产生1-100的随机数
    r = random.randint(1, 100)
    position = bisect.bisect(l, r)
    bisect.insort(l, r)
print'%3d  %3d' % (r, position), l



CONSTANT = 0
def modifyConstant() :
        global CONSTANT
        print CONSTANT
        CONSTANT += 1
        return
if __name__ == '__main__' :
        modifyConstant()
        print CONSTANT