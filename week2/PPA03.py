t=int(input())
if(t>=24):
    print("INVALID")
elif(t>=18):
    print("EVENING")
elif(t>=12):
    print("AFTERNOON")
elif(t>=6):
    print("MORNING")
elif(t>=0):
    print("NIGHT")
else:
    print("INVALID")