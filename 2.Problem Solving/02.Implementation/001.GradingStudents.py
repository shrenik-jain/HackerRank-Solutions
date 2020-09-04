import math
import os
import random
import re
import sys

def gradingStudents(grades):
    # Write your code here
    for i in grades:
        if i%5 > 2 and i>=38:
            print(i-i%5+5)
        else:
            print(i)  

if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    gradingStudents(grades)
