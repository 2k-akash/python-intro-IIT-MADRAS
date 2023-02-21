'''
Accept a sequence of comma-separated words as input. Reverse the sequence and print it as output.
'''
L = input().split(',')

rev = []
for i in range(len(L)-1,-1,-1):
    rev.append(L[i])
for i in range(len(rev)):
    if (i != len(rev)-1):
        print(rev[i],end = ",")
    else:
        print(rev[i])