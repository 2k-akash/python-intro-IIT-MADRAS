#multiplication table 1
'''
num = int(input())
for i in range(1,11):
    print(num,'X',"=",num*i)

#multiplication table 2

for i in range(1,11):
    print("2X",i,"=",2*i)

#multiplication table 3
num = int(input())
for i in range(1,11):
    print(f'{num}X{i}={num*i}')

#multiplication table 4
num =int(input())
for i in range(1,11):
    print(num,'X',i,"=",num*i)'''

#multipliction table using format function

num =int(input())
for i in range(1,11):
    print('{0}X{1}={2}'.format(num,i,num*i))


#multiplication table using string modulo operator

num = int(input())
for i in range(1,11):
    print('%d X %d = %d'%(num,i,num*i))




