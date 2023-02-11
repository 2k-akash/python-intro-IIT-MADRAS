n = int(input())
choices = int(input())
correct = input()
c = (len(correct) + 1) // 2
selected = input()
marks = 0.0
for i in range(0,len(selected),2):
    if selected[i] in correct:
        marks = marks + n/c
    else:
        marks = 0.0
        break
print(marks)