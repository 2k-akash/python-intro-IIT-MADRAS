n1 = input()
d1 = input()
n2 = input()
d2 = input()

d1 = d1[6:] + "-" + d1[3:5] + "-" + d1[:2]
d2 = d2[6:] + "-" + d2[3:5] + "-" + d2[:2]
if d1 > d2:
    print(n1)
elif d1 < d2:
    print(n2)
else:
    if n1 < n2:
        print(n1)
    else:
        print(n2)

