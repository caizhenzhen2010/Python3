leaps=[]
for year in range(0,1940):
    if(year%4==0 and year%100!=0)or(year%400==0):
            leaps.append(year)

print(leaps)