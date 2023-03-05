def list_average(l):
    sum = 0
    for i in range(len(l)):
        sum = sum + l[i]
    ans = sum /len(l)
    return ans
l = [7,8,9,10]
print(list_average(l))