#Palindrome or not

word = input()
reverse = ""
for char in word:
     reverse = char +reverse

if (reverse == word):
    print("PALINDROME")
else:
    print("NOT PALINDROME")