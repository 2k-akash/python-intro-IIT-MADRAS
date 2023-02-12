#Accept a string as input, convert it to lower case,
#sort the string in alphabetical order,and print the sorted string to the console

s = input().lower()

a = 'abcdefghijklmnopqrstuvwxyz'
t = ''
for x in a:
    for y in s:
        if (x == y):
            t +=y
print(t)