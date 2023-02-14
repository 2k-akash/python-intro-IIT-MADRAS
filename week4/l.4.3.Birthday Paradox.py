import random
l = []
for i in range(100):
    l.append(random.randint(1,10))
print(l)
i =0
flag = 0
while(i < len(l)- 1):
    if (l[i] == l[i+1]):
        print("Repeats",l[i],l[i+1])
        flag =1
        break
     i = i + 1
if (flag == 0):
    print("No Repetition")






