'''
Accept a square matrix as input and store it in a variable named matrix.
The first line of input will be n the number of rows in the matrix.
Each of the next n lines will have a sequence of
n space-separated integers.
'''
n = int(input())
matrix = []
for i in range(n):
    L = []
    for num in input().split(' '):
        L.append(int(num))
    matrix.append(L)
print(matrix)