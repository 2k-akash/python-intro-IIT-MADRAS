'''
A list L of words is already given to you as a part of the prefix code.
Print the longest word in the list.
If there are multiple words with the same maximum length,
print the one which appears at the rightmost end of the list.
'''

L = input().split(',')
max_word, max_len = '',0
for i in L:
    if (len (i) >= max_len):
        max_word = i
        max_len = len(i)
print(max_word)