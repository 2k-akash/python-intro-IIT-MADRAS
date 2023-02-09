#No of digits in the given no

num = abs(int(input("Enter a no")))
strNum = str(num)
digits = 0
for c in strNum:
    digits = digits + 1
print(digits)