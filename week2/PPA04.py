a=float(input())
b=float(input())
if a>0 and b>0:
    print("first")
elif a<0 and b>0:
    print("second")
elif a<0 and b<0:
    print("third")
elif a>0 and b<0:
    print("fourth")
elif a>0 and b==0:
    print("x-axis")
elif a==0 and b<0:
    print("y-axis")
else:
    print("origin")


