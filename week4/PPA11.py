# sort the list using function
def solution (L):
    elem = 0
    sorted_L = []
    while L != []:
        max_elem = L[0]
        if (elem >= max_elem):
            max_elem = elem
    L.remove(max_elem)
    sorted_L.append(max_elem)
    return sorted_L


