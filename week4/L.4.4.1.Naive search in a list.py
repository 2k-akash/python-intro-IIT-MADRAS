import random
l = []
a = 5
for i in range(10000):
    l.append(random.randint(1,10000))
flag = 0
for i in range(len(l)):
    if (a == l[i]):
        print("hurray,Element found")
        flag = 1
        break
if (flag == 0):
    print("Element not found")