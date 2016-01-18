
def foo(name,action="eat",*args,**keywords):
    print name,action
    for item in args:
        print item
    print keywords.keys()
    
foo('ccc')
foo('zzz','drink',1,2,3,a=1)