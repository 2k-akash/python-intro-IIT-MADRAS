#break
'''
email = input()
for c in email:
    if( c =="@"):
        break
    print(c,end = " ")

# continue
email = input()
for c in email:
    if (c == "@"):
        print(' ')
        continue
    print(c,end="")'''

#printing all nos which are / by 3
for x in range(11):
    if (x % 3 == 0):
        print(x,end = "")
    else:
        pass