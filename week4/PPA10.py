n = int(input())
A = [] # A matrix
for i in range(n):
    row = []
    for x in input().split(' '):
        row.append(int(x))
    A.append(row)

B = [] #B matrix
for i in range(n):
    row = []
    for x in input().split(' '):
        row.append(int(x))
    B.append(row)

C = [] #C matrix
for i in range(n):
    row = []
    for j in range(n):
        row.append(0) #make the entries in the matrix as 0
    C.append(row)

for i in range(n):
    for j in range(n):
        C[i][j] = A[i][j] + B[i][j] # adding A and B matrix and stor it to the C matrix
        if (j != n-1):
            print(C[i][j],end = ',')
        else:
            print(C[i][j])