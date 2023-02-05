#A class teacher decided to split her entire class into four groups
#namely Sapphire, Peridot, Ruby, and Emerald.

roll = int(input())
if (roll % 4 == 0):
    print("Emerald")
elif (roll % 4 == 1):
    print("Sapphire")
elif (roll % 4 == 2):
    print("Peridot")
elif (roll % 4 == 3):
    print("Ruby")