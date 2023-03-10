# sort the list using function
def solution (L):
    sorted_L = []
    while L != []:
        max_elem = L[0]
        for elem in L:
            if (elem >= max_elem):
                max_elem = elem
        L.remove(max_elem)
        sorted_L.append(max_elem)
    return sorted_L



