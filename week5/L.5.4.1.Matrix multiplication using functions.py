#initialize the matrix
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