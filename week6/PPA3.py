'''
(1) is_key: accept a dictionary D and a variable key as arguments.
    Return True if the variable key is a key of the dictionary D, and False otherwise.

(2) value: accept a dictionary D and a variable key as arguments.
    If the variable key is not a key of the dictionary D, return None, otherwise, return the value corresponding to this key.
'''
def is_key(D,key):
    return key in D
def value(D, key):
    if is_key in D:
        return D[key]
    else:
        return None
