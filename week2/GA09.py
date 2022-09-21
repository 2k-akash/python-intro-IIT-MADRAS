#accepts a sentence as input and prints the number of words in it.
# A sentence is just a sequence of words with a space between consecutive words.
# You can assume that the sentence will not have any other punctuation marks.
# You can also assume that the input string will have at least one word.
sentence = input()
space = ' ' # there is a single space between the quotes
num_words = sentence.count(space)
print(num_words)


