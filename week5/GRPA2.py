'''
Write a function named is_perfect that accepts a positive integer
n as argument and returns True if it is perfect, and False otherwise.
'''
def is_perfect(n):
    fsum = 0
    for f in range(1, n):
        if (n % f == 0):
            fsum = fsum + f
    return fsum == n

