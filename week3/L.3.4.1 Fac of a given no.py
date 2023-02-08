#find the factorial of the given no
num = int(input("Enter a no:"))
fact = 1
if(num<0):
    print("Not defined")
else:
    while(num>0):
        fact = fact* num
        num =num-1
    print(fact)