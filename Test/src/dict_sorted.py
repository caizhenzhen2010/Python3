#! /usr/bin/python2.7
#! encoding:utf-8

mydict={'a':100,'c':20,'b':200}
print sorted(mydict.items(),key=lambda mydict:mydict[1])
print sorted(mydict.items(),key=lambda mydict:mydict[1],reverse=True)
print sorted(mydict.items(),key=lambda mydict:mydict[0])
print sorted(mydict.items(),key=lambda mydict:mydict[0],reverse=True)
print sorted(mydict.items(),key=lambda mydict:mydict[0],reverse=True)

l = [] 
d = {'num': 0, 'sqrt': 0} 
for x in [1, 2, 3]: 
    d['num'] = x 
    d['sqrt'] = x*x 
    l.append(d) 
    print l