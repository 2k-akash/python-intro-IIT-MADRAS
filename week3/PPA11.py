#pythaorean triplet

n=int(input())
if (n > 5):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if (i **2 +j ** 2 == k**2 and i<j<k):
                    print(i,j,k,sep =",")
                    break
else:
    print("NO SOLUTION")

