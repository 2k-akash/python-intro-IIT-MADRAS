'''
Accept a positive integer n as input and
print the list of n positive integers as input
'''
n = int(input())
L = []
for i in range(1, n+1):
    L.append(i)
print(L)