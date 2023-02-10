#Accept a positive integer as input
#print the sum of the digits in the number

n = input()
sum = 0
for i in n:
    sum += int(i)
print(sum)