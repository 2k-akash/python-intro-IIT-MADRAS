# L is a positive integer that has already been defined at this stage
word = input()
l=5
space = ' ' # there is a single space
if len(word) < l:
    word = 'short' + space + word
elif l <= len(word) < 2 * l:
    word = 'medium' + space + word
else:
    word = 'long' + space + word
print(word)