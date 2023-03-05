def upper(s):
    upper = 0
    for c in s:
        if (c.isupper()):
            upper +=1
    return (upper)
s = 'AKASH'
print(upper(s))

def lower(s):
    lower = 0
    for c in s:
        if c.islower():
            lower +=1
    return lower
s = 'akASh'
print(lower(s))