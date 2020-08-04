#bin/python3

import math
import os
import random
import re
import sys

n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

print(arr)

i = 0
sum1 = 0
sum2 = 0
for line in arr:
#    print('Line: ',i, 'value:', line[i])
    sum1 = line[i] + sum1
    i = i + 1
for line in arr:
    i = i - 1
    sum2 = line[i] + sum2
    print('Line: ',i, 'value:', line[i])

print('Sum1=', sum1)
print('Sum2=', sum2)

ans = sum1-sum2
print('Answer:', abs(ans))
