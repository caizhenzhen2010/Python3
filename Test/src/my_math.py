#! /usr/bin/env python
#！ -*- decoding:utf-8 -*-
def square(x):
    """
    Square a number and return the result.
    
    >>> square(2)
    4
    >>> square(4)
    16
    
    """
    return x*x
#>>>符号之后要空格

def product(x,y):
    """
    return x*y
    """
    return x*y


if __name__=='__main__':
    import doctest,my_math
    doctest.testmod(my_math)
