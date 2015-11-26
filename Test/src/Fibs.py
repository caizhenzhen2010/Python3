class Fibs:
    def __init__(self):
        self.a=0
        self.b=1
    def next(self):
        self.a,self.b=self.b,self.a+self.b
        return self.a
    def __iter__(self):
        return self
    
fibs=Fibs()
for fib in fibs:
        print fib
        print '\n'
        if fib>10000:
            break

it=iter([1,2,3])
print it.next()
print it.next()
print it.next()
print it.next()