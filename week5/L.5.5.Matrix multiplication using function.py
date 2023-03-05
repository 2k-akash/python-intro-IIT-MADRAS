def initialize_mat(dim):
    C = []
    for i in range(dim):
        C.append([])
    for i in range(dim):
        for j in range(dim):
            C[i].append(0)
    return C
dim = 3
print(initialize_mat(dim))

def dot_product(u,v):
    dim = len(u)
    ans = 0
    for i in range(dim):
        ans = ans + (u[i] * v[i])
    return ans
u = [1,2,4],[2,3,4]
v= [5,8,9],[7,6,5]
print(dot_product(u,v))
def row(M,i):
    dim = len(M)
    l = []
    for k in range(dim):
        l.append(M[i][k])
    return l
M = [[1,2,3][34,5,6]]
i =0
def column(M,j):
    dim = len(M)
    l = []
    for k in range(dim):
        l.append(M[k][j])
    return l
M = [[1,2,3],[34,5,6]]
j =0

def mat_mul(A,B):
    dim = len(A)
    C = initialize_mat(dim)
    for i in range(dim):
        for j in range(dim):
            C[i][j] = dot_product(row(A,i),column(B,j))
    return C
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[4,5,6][3,4,5],[5,6,7]]