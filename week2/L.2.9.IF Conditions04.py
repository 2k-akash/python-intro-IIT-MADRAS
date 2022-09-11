#convert the given flow chart into python code
print("Travel from City A TO City B")
Time=int(input("Enter time:"))
Longer=int(input("define longer:"))
if(Time>=Longer):
    Price=int(input("Enter Price:"))
    Higher=int(input("define higher:"))
    if(Price>=Higher):
        print("Train")
    else:
        print("Coach")

else:
    Price=int(input("Enter Price:"))
    Higher=int(input("define higher:"))
    if(Price>=Higher):
        print("Daytime flight")
    else:
        print("Red Eye Flight")
print("Arrive City B")