#input will be four integers in four lines
#The output should be a single line with all the integers separated by a single space in non decreasing order
#there is no space after the fourth integer.

a = int(input())
b = int(input())
c = int(input())
d = int(input())
numbers = [a,b,c,d]
numbers.sort()
print(*numbers)
