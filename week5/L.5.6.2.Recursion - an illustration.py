# to find the factorial
def fact(n):
    if (n == 1):
        return 1
    else:
        return fact(n-1) * n
n = 5
print(fact(n))

def comp(p,n):
    if n==1:
        return p *(1.1)
    else:
        return (comp(p,n-1) * 1.1)
p = 1000
n = 10
print(comp(p,n))