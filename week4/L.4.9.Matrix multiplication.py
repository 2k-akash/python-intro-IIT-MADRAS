'''
r1 = [1,2,3]
r2 = [4,5,6]
r3 = [7,8,9]

s1 = [1,2,1]
s2 = [6,2,2]
s3 = [4,2,1]

A = []
B = []

A.append(r1)
A.append(r2)
A.append(r3)

B.append(s1)
B.append(s2)
B.append(s3)

C = [[0,0,0],[0,0,0],[0,0,0]]
dim = 3
for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            C[i][j] = C[i][j] + A[i][k]* B[k][j]
print(C)'''
import numpy
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[1,2,1],[6,2,3],[4,2,1]]

X = numpy.mat(A)
Y = numpy.mat(B)

print(X*Y)
