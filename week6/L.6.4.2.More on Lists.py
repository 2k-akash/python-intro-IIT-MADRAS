l1 = [1,2,3]
'''l2 = list(l1)
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

l = [1,2,3]
print(l)
l.append(4)
print(l)
l.remove(2)
print(l)

x = l.copy()
print(x,l)
'''
print(l1.pop(2))


l = [2,6,1,50,3,7,5]

l.insert(2,55555)
print(l)
