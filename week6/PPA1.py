'''
Accept a sequence of words as input.
Create a dictionary named freq whose keys are the distinct words in the sequence.
The value corresponding to a key (word) should be the frequency of occurrence of the key (word) in the sequence.
'''


freq = dict()
L = input().split(',')
for word in L:
    freq[word] = 0
for word in L:
    freq[word] += 1
print(freq)