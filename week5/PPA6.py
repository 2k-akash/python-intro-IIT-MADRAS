'''
A class of English words is called mysterious if it satisfies certain conditions.
These conditions are hidden from you.
Instead, you are given a function named mysterious that accepts a word as argument and returns True if the word is mysterious and False otherwise.


'''
def type_sequence(L):
    k = 0
    for i in range(len(L)):
        if mysterious L[i]:
            k = k+1
    if k < 2:
        return 'mildly mysterious'
    elif k < 5:
        return 'moderately mysterious'
    else:
        return 'most mysterious'