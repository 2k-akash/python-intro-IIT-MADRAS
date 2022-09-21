'''E is a Boolean expression.
Two blocks of code are said to be equivalent
if they produce the same output for a given input.'''

#Block-1
E=False
if E:
    print('good')
else:
    print('bad')

#Block-2
E=False
if E:
    print('good')
print('bad')

#Block-3
print('good')
print('bad')