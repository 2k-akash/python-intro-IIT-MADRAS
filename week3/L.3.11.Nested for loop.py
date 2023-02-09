'''
s = "VIBGYOR"
for i in range(7):
    print(s[i],end = " ")'''

s = "VIBGYOR"
t = "VIBGYOR"
count = 0

for i in range(7):
    for j in range(7):
        print(i,j,s[i],s[j])
        count = count + 1
    print("Total ways in which the two brothers can wear 7 different colors:",count)