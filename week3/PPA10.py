#Accept positive integer as input and print the sum of all prime numbers in the range[1,n]
#if thre are no prime numbers print 0

n = int(input())
sum = 0
for i in range(1, n+1):
    count = 0
    for j in range(1,i+1):
        if (i % j == 0):
            count = count +1
    if (count == 2):
        sum = sum + i
print(sum)
