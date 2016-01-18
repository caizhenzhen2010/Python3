#! /usr/bin/python2.7
#! encoding:utf-8

'''
Create on 2015,1,5
@author: sean
'''

def func1():
    print 'func1'
    func2()
    
def func2():
    print 'fuc2'
    
if __name__=='__main__':
   print 'index',
   func1()
else:
    print 'module'
    print __name__
 

