#remove all the characters in b
#which are present in a
#accept two strings

a = input()
b = input()
str = ""
for i in b:
    if i not in a:
        str = str + i
print(str)
