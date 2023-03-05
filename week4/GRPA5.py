#To find the average
def list_average(l):
    sum = 0
    for i in range(len(l)):
        sum = sum +l[i]
    ans = sum /len(l)
    return ans
l = [1,23,45,678,34]
print(list_average(l))