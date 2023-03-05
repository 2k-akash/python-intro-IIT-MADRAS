'''def row(M,i):
    dim = len(M)
    l = []
    for k in range(dim):
        l.append(M[i][k])
    return l
M = [[1,2,3],[4,5,9],[3,3,3]]
i = 1
print(row(M,i))'''

def col(M,j):
    dim = len(M)
    l = []
    for k in range(dim):
        l.append(M[k][j])
    return l
M = [[1,2,4],[4,6,7],[5,6,90]]
j = 1
print(col(M,j))