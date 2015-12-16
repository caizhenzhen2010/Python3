a=[]
for num in range(2,1001):
    result=True
    i=2
    while i <num:
        if num%i==0:
            result=False
            break
        i+=1
    if result:
        a.append(num)
       
print a
    