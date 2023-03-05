'''
Write a function named factorial that accepts an integer n as argument.
It should return the factorial of n if n is a positive integer.
It should return -1 if n is a negative integer,
and it should return 1 if n is zero.
'''

def factorial(n):
    if n < 0:
        return -1
    elif (n == 0):
        return 1
    else:
        f = 1
        for i in range(1, n+1):
            f *= i
        return f
n = 5
print(factorial(n))