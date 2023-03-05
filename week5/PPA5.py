def dim_equal(A,B):
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        return True
    else:
        return False

A =[[1,2],[3,4]]
B = [[3,5],[4,3]]
print(dim_equal(A,B))