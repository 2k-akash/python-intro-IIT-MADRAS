malgudi=['It','was','monday','morning','Swaminathan','was ', 'reluctant','to ','open','his','eyes' ,'he','considered','Monday' ,'specially','unpleasant', 'in ','the','calendar','It','was' ,'Monday']
s =set(malgudi)
#print(s)
#print(len(s))
#print(malgudi)
#print(len(malgudi))

'''max = 0
d = {}
for x in s:
    d[x] = 0

for x in malgudi:
    d[x] = d[x] +1
    if d[x] > max:
        max = d[x]
print(max)
'''

d = {}
for x in s:
    d[x] = 0
max = 0
ans = ''
for x in malgudi:
    d[x] = d[x] + 1
    if d[x] > max:
        max = d[x]
        ans  = x
print(max)
print(ans)

