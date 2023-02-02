s = input()
length = len(s)
if (length % 2 == 0):
    if (s[-1] == "."):
        s = s[:-1]
    else:
        s = s + "."
middle = len(s)//2
print(s[middle-1:middle+2])





