n = int(input())
I = []
for i in range(n):
    row = []
    for j in range(n):
        if (i == j):
            row.append(1)
        else:
            row.append(0)
    I.append(row)
for i in range(n):
    for j in range(n):
        if j != n -1:
            print(I[i][j],end = ',')
        else:
            print(I[i][j])
