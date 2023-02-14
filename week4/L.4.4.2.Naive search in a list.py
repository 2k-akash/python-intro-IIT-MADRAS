import random
l = []
for i in range(100):
    l.append(random.randint(1,1000))
n = 0
while (n > -1):
    print('Enter a no,type -1 to exit')
    n = int(input())
    flag = 0
    for i in range(len(l)):
        if (n == l[i]):
            print("element found")
            flag = 1
            break
    if (flag == 0):
        print('element not found')