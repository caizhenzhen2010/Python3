import random
for i in range(6):
    if i==random.randint(1,5):
        print random.randint(0,9)
    else:
        print chr(random.randint(65,117))