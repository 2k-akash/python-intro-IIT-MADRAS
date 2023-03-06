'''
x = [1,4,5,5]
y = {1,24,5,8,9}
print(type(x))
print(type(y))
print(x)
print(y)
'''

'''
l = list(range(100))
s = set(range(100))
print(l)
print(s)
'''
import sys
l = []
l1 = [0]
l2 = [0,1]
print(sys.getsizeof(l))
print(sys.getsizeof(l1))
print(sys.getsizeof(l2))



x = list(range(100))
y = set(range(100))
print(sys.getsizeof(x))
print(sys.getsizeof(y))


z = {'amit','nehru','anamika','varsha','nitin'}
print('amar' in z)
print('anamika' in z)
print('nitin' in z)
print('sudharsan' in z)

z.add('karthik')
print(z)




