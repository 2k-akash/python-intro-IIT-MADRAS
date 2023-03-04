'''
You are given a list marks that has the marks scored by a class of students in a Mathematics test.
Find the median marks and store it in a float variable named median.
You can assume that marks is a list of float values.
'''

def solution (marks):
    sorted_marks = []
    while marks != []:
        min_marks = marks[0]
        for mark in marks:
            if mark < min_marks:
                min_marks = mark
        marks.remove(min_marks)
        sorted_marks.append(min_marks)
    n = len(sorted_marks)
    if n % 2 == 0:
        mid = n//2
        median = sorted_marks[mid]
    else:
        mid2 = n//2
        mid1 = mid2 - 1
        median = (sorted[mid1] +sorted[mid2])/2
    return median









