l = [12,10,2,16,98,561,3]
x =[]
while(len(l) > 0):
    min = l[0]
    for i in range(len(l)):
        if l[i] < min :
            min = l[i]
    x.append(min)
    l.remove(min)
print(l)
print(x)