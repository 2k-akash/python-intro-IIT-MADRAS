'''
Write a function named distance that accepts two words as arguments and returns the distance between them.

'''
def distance(word_1, word_2):
    if len(word_1) != len(word_2):
        return -1
    letters = 'abcdefghijklmnopqrstuvwxyz'
    size = len(word_1)
    dist = 0
    for i in range(size):
        c1, c2 = word_1[i], word_2[i]
        d = abs(letters.index(c1) - letters.index(c2))
        dist = dist + d
    return dist
word_1 = 'akash'
word_2 = 'suraj'
print(distance(word_1,word_2))

