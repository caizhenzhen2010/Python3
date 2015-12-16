#! /usr/bin/python2.7
# -*- encoding: utf-8 -*-

def foo1(arg1,arg2,key1=1,key2=2,*arg,**keywords):
    print "arg1 parameters is ",arg1
    print "arg2 parameters is ",arg2
    print "key1 parameter is ",key1
    print "key2 parameter is ",key2
    print "Arbitrary parameter is ", arg
    print "keywords parameter is ",keywords

foo1(1,2,3,4,5,6,k1=1,k2=2,k3=3)
foo1(1,2,5,6,k1=1,k2=2,k3=3)
foo1(1,2,k1=1,k2=2,k3=3)