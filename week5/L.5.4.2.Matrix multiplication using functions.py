def dot_product(u,v):
    dim = len(u)
    ans = 0
    for i in range(dim):
        ans = ans +(u[i] * v[i])
    return ans
u = [1,3,45,67]
v = [23,45,68,90]
print(dot_product(u,v))