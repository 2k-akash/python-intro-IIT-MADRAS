#Accept a sequence of words and print the shortest word

str = input()
min_str = str
while (str != "abcdefghijklmnopqrstuvwxyz"):
    str = input()
    if (len(str) < len(min_str)):
        min_str = str
print(min_str)
