'''hire the person if backlog shoul atmost 5 a
and cgpa should greater than 6,salary is five times
the cgpa'''


bl=int(input())
cgpa=float(input())
if bl<=5 and cgpa>6:
    print(cgpa*5)
else:
    print("Not Selected")