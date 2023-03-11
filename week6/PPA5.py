def dict_to_list(D):
    L = []
    for key in D:
        L.append((key,D[key]))
    return L


def list_to_dict(L):
    D = dict()
    for key,value in L:
        D[key] = value
    return D
D = {'abc': 3, 'def': 10}
L = [('def', 10),('abc', 3)]
print(dict_to_list(D))
print(list_to_dict(L))