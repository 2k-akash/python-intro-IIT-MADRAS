#To append before

def list_appendbefore(l,z):
    newl =[]
    for i in range(len(z)):
        newl.append(z[i])
    for i in range(len(l)):
        newl.append(l[i])
    return newl

l = [1,2,3,45,6,7,89]
z = [10,20,30]
print(list_appendbefore(l,z))

#To append the list at th end
def append_end(l,z):
    newl =[]
    for i in range(len(l)):
        newl.append(l[i])
    for i in range(len(z)):
        newl.append(z[i])
    return newl
l = [1,3,5,6,7,90,34]
z = [3,5,6,723,90]
print(append_end(l,z))