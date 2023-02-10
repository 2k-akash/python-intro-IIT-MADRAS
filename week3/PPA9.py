#Accept a positive integer n as input
#print triangle of zeros for n lines
'''n=int(input())

for i in range(n+1):
    print("0"* i)'''
num = int(input())
for i in range(num):
    for j in range(i+1):
        print(str(0),end="")
    print("")