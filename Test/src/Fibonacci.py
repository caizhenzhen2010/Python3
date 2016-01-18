'''
def foo(max):
    n, a, b = 0, 0, 1
    while n<max:
        print b
        a, b = b, a+b
        n+=1
foo(5)
'''
'''
def foo(max):
    n , a, b = 0, 0, 1
    L=[]
    while n<max:
        L.append(b)
        a, b = b , a+b
        n+=1
    return L

i=foo(5)
print i
'''

'''
def foo(max):
    n, a, b = 0, 0, 1
    while n<max:
        yield b
        a, b = b, a+b
        n+=1
re=foo(5)
print re.next()
print re.next()
print re.next()
print re.next()
print re.next()
print re.next()
'''
def alexreadlines():
     with open(__file__,'rb') as f:
        while True:
             line = f.readline()
             if line:
                 yield line
             else:
                      return 
for line in alexreadlines():
    print line