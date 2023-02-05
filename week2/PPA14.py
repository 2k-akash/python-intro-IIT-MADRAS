word = input()
present = False
if ('a' in word and 'e' in word and 'i' in word and 'o' in word and 'u' in word):
    if (word.index('a') < word.index('e') < word.index('i') < word.index('o') < word.index('u')):
        if (word.count('a') >= word.count('e') >= word.count('i') >= word.count('o') >= word.count('u')):
            present = True
if (present):
    print("It is a perfect word")
else:
    print("It is not a perfect word")