a = abs(int(input()))
b = abs(int(input()))
sum = 0
for i in range(1000,2001): #range[1000,2000]
    if( i%a == 0 and i%b == 0):#the points that are divisible by both a and b
        sum = sum + i
print(sum)
