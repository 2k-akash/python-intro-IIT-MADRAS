A = {1,3,5}
B = {2,4,5}
print(A.issubset(B))
print(A.intersection(B))
print(A.union(B))
print(A.difference(B))
C1 = A.intersection(B)
C2 = A & B
print(C1, C2)