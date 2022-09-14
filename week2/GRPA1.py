'''Accept three positive integers as input and check if they form the sides of a right triangle.
 Print YES if they form one, and NO if they do not.
The input will have three lines, with one integer on each line.
The output should be a single line containing one of these two strings: YES or NO.'''


x=int(input())
y=int(input())
z=int(input())
a=x*x+y*y
b=z*z
if(a==b):
    print("YES")
else:
    print("NO")
