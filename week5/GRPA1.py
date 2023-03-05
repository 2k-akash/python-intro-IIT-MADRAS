def get_max(L):
    max = L[0]
    for x in L:
        if x > max:
            max = x
    return x

def get_min(L):
    min = L[0]
    for x in L:
        if x < min:
            min = x
    return x
def get_range(L):
    mini = get_min(L)
    maxi = get_max(L)
    return maxi -mini
