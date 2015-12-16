#! /usr/bin/python2.7
# -*- encoding: utf-8 -*-

a=[2,3,4,4]
try:
    print a[100]
except IndexError:
    print 'indexerror'
print 'continue'
