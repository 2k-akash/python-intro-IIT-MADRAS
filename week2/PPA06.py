s = input()
s1 = len(s)
s2 = ''
s3 = ''
if (s1 % 2 == 0):
    if not (s.endswith('.')):
        s2 = s + '.'
    if (s.endswith('.')):
        s2 = s.strip(s[s1 - 1])
    i = (len(s2) + 1) // 2
    s3 = s2[i - 2] + s2[i - 1] + s2[i]
    print(s3)
else:
    i = (len(s) - 1) // 2
    s2 = s[i - 1] + s[i] + s[i + 1]
    print(s2)




