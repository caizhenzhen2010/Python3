#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Create on 2016年1月9日
@author: sean
'''
from xmlrpclib import _decode
'''
import time
def my_deco(func):
    print func
    return func

@my_deco
def foo():print 'execting foo()'

foo()


def deco_needdoc(func):
    def _deco_needdoc():
        func()
        if func.__doc__==None:
            print func,'has no doc ,it is a bad habit'
        else:
                print 'func has doc',func.__doc__
    return _deco_needdoc

@deco_needdoc
def f():
    print 'f func has no doc'
@deco_needdoc
def g():

    print 'g func has doc'

f()
g()
'''
    
def deco(arg):
    def _deco(func):
        def __deco():
            print 'before %s call ,%s called.'%(func.__name__,arg)
            func()
            print 'after %s called'%func.__name__
        return __deco
    return _deco
@deco('mymodule')
def myfun1():
    print 'my fun1 called'
@deco('mymodule2')
def myfun2():
    print 'my fun2 called'

myfun1()
myfun2()
@staticmethod
    