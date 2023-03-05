#to find the min in the list
def list_min(l):
    mini = l[0]
    for i in range(len(l)):
        if (l[i] < mini):
            mini = l[i]
    return mini
l=[5,67,4,345,2]
print(list_min(l))

#To find the maximum in the list
def list_max(l):
    max = l[0]
    for i in range(len(l)):
        if l[i] > max:
            max = l[i]
    return max
l=[1,2,45,3]
print(list_max(l))