'''print("When did India get its independence?")
year=int(input())

if(year==1947):
    print("hip hip hurray.You got that right")
else:
    print("Comeon dont you know even this?")
    print("Thats ok,I will let you attempt this once more")
    print("When did India get its independence?")
    year=int(input())
    if (year==1947):
        print("You got it!")
    else:
        print("Failed in your second attempt too?grrr..")'''

#using while loop
print("when  did India get its Independence(year)?")
year=int(input())

while(year!=1947):
    print("you got this wrong.Enter once again.")
    year=int(input())
print("wow..you got it right")

