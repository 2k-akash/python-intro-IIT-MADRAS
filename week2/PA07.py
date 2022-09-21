x=0
bool_var=True
if bool_var:
    x = x + 1
    bool_var = not bool_var
    if bool_var:
        x = x + 1
    else:
        x = x - 1
print(x)