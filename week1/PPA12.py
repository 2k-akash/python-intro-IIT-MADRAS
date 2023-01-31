'''replicating the substring a minimum number of times
so that the resulting string is longer than the input string'''
s=input()
start=int(input())
end=int(input())
ls=len(s)
sb=s[start:end+1]
lsb=len(sb)
n=(ls//lsb)+1
print(sb*n)