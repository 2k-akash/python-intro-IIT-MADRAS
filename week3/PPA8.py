#Accept a positive integer n as input
#print the first n integers on a line separated by a comma
num = int(input())
for i in range(1, num+1):
    if (i != num):
        print(i,end=",")
    else:
        print(i)
