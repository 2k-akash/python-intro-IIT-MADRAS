alpha='abcdefghijklmnopqrstuvwxyz'
s='rizwan'
t=''
i=0
k=1
t=t+(alpha[(((alpha.index(s[i]))+k)%26)])
t=t+(alpha[(((alpha.index(s[i+1]))+k)%26)])
t=t+(alpha[(((alpha.index(s[i+2]))+k)%26)])
t=t+(alpha[(((alpha.index(s[i+3]))+k)%26)])
t=t+(alpha[(((alpha.index(s[i+4]))+k)%26)])
t=t+(alpha[(((alpha.index(s[i+5]))+k)%26)])

print(t)