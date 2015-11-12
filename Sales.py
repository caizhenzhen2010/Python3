import sys
import collections
Sale = collections.namedtuple("Sale","productid customerid date quantity price")
sales=[]
sales.append(Sale(432,921,"2008-9-14",3,7.99))
sales.append(Sale(432,921,"2009-9-14",3,7.99))
total=0
for sale in sales:
	total+=sale.quantity*sale.price
print("Total${0:2f}".format(total))