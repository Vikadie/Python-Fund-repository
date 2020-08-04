import math
import os
import random
import re
import sys

b = [72, 48]

a = [1]
print('a before:', a)

x = max(a)
print('x= ', x)
print('min(b)', min(b))

ans = 0
lst = list()

for xi in a:
    if x >= min(b): break
    for yi in a:
        x = xi*yi
        if x >= min(b): break
        if x not in lst: lst.append(x)

print('a after', a)
print('lst after', lst)


for i in b:
    print('i in b = ', i)
    an = 0
    for j in lst:
        print('j in a=', j)
        if i%j == 0: an = an + 1
        print('an=', an, 'len(a) = ', len(a))

    if an >= len(a):
        ans = ans + 1
    print('ans', ans)
print('ans', ans)
