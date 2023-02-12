a = input()
b = input()
n1 = len(a)
n2 = len(b)
n = n1 + n2
word = ''
while (n > 0):
    if len(a) == 0:
        word = word + b
        break
    elif len(b) == 0:
        word = word + a
        break
    else:
        if (a[0] == b[0]):
            word = word + a[0] * 2
            a = a[1:]
            b = b[1:]
            n -= 2
        elif a[0] > b[0]:
            word = word + b[0]
            b = b[1:]
            n -= 1
        else:
            word = word + a[0]
            a = a[1:]
            n -= 1
print(word)
