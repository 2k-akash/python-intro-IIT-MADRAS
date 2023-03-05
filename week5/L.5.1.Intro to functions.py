#discount problem
def discount(cost,d):
    ans = cost - (cost * (d/100))
    return ans

cost = int(input())
d = int(input())
ans = discount(cost,d)
print(ans)