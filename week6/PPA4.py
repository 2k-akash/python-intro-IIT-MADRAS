def value_to_keys(D, value):
    values = []
    for key in D:
        if D[key] == value:
            values.append(key)
    return values

D = {1: 10, 2: 100, 3: 1000, 4: 10}
value = 10
print(value_to_keys(D,value))