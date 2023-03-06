l1 = [1,2,3]
l2 = list(l1)
l3 = l1[:]
l4 = l1.copy()

l2[0] = 100
l3[1] = 200
l4[2] = 300
print(l1,l2,l3,l4)



print(l1 is l2)
print(l2 is l3)
print(l1 is l4)
print(l1 is l3)


def add(x):
    x = x+1
    return x
x =1
print(add(x))
