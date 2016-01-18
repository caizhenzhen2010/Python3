import pickle
mylist=['ls',1,2,3,4]
dumpsed=pickle.dumps(mylist)
print dumpsed
undumps=pickle.loads(dumpsed)
print undumps

pickle.dump(mylist, open('pickle_list.txt','wb'))


import json
print type(json.dumps(mylist))

