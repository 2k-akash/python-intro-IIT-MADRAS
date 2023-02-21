'''Accept a sequence of comma-separated integers as input and print the maximum value in the sequence as output.'''
n = input()
L = n.split(',')
max = int(L[0])
for i in L:
    i = int(i)
    if (i > max):
        max = i
print(max)

