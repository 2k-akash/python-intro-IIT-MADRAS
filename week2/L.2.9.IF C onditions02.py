#find whether the given number ends with 0 or 5 0r any other
num=int(input("Enter a Number:"))
if(num%5==0):
    if(num%10==0):
        print("0")
    else:
        print("5")
else:
    print("Other")