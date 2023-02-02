a = input()
b = input()
c = input()
d = input()
e = input()
'''if a in b and b in c and c in d and d in e:
    print("magical")
else:
    print("non-magical")'''
flag = "non-magical"
if a in b:
    if b in c:
        if c in d:
            if d in e:
                flag = "magical"
print(flag)
