def character(s):
    chars = 0
    for c in s:
        chars +=1
    return chars
s ='rrrrrrrr'
print(character(s))

def word(s):
    word = 0
    for c in s:
        if (c == ''):
            word +=1
    return (word)
s = 'Akash','uhan'
print(word(s))