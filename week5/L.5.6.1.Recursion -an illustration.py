#to find the sum

def sum(n):
    ans = 0
    for i in range(n):
        ans = ans + (i+1)
    return ans
n = 34
print(sum(n))

def sum(n):
    if (n == 1):
        return 1
    else:
        return n+sum(n-1)