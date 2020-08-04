import math
import os
import random
import re
import sys

grades = [73, 67, 38, 33]

print('Grades before are: ', grades)

i = -1

for grade in grades:
    i = i + 1
    if grade < 38 : grades[i] = grade
    else:
        g = grade/5
        ans = math.ceil(g)
        if  round(g) == ans: grades[i] = round(g)*5
        else: grades[i] = grade

print('Grades after are (based on rule of Sam found in Hackerrank): ', grades)
