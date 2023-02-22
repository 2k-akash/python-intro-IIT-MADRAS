'''
first line - accept a sequence of space-separated words.
second line -accept a single word.
If this word is not present in the sequence, print NO.
If this word is present in the sequence, then print YES and in the next line of the output,
print the number of times the word appears in the sequence.
'''

s = input().split(' ')
a = input()
if a   in s:
    print('YES')
    print(s.count(a))
else:
    print('NO')

