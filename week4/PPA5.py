'''
Accept a space-separated sequence of positive real numbers as input.
Convert each element of the sequence into the greatest integer less than or equal to it.
Print this sequence of integers as output, with a comma between consecutive integers.
'''

L = input().split(' ')
for i in range(len(L)):
    L[i] = float(L[i])
    L[i] = int(L[i])

for i in range(len(L)):
    if (i != len(L)-1):
        print(L[i],end = ",")
    else:
        print(L[i])