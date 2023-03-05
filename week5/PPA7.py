#accept a list as argument
# if empty list
def is_empty(l):
    if len(l) == 0:
        return True
    else:
        return False
l = []
print(is_empty(l))


#first(l)
def first(l):
    if not is_empty(l):
        return l[0]
    else:
        return 'None'
l = [1,3,4]
print(first(l))

#last(l)
def last(l):
    if not is_empty(l):
        return l[-1]
    else:
        return 'None'
l = [1,4,5]
print(last(l))

#init(l)
def init(l):
    if not is_empty(l):
        return l[:-1]
    else:
        return 'None'
l = [1,2,3,4,5]
print(init(l))
#rest(l)
def rest(l):
    if not is_empty(l):
        return l[1:]
    else:
        return 'None'
l = [1,3,45,5]
print(rest(l))


