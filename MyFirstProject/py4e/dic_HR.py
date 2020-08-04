import re
import sys
import os
import math

h = int(input())
dic = {}
for i in range(h):
    ddd = input().rstrip().split()
    dic[ddd[0]] = ddd[1]

print("ddd", ddd)
print("Dic", dic)


#for key in dic: -- Wrong!
#for i in range(h): -- replace with while True and try/except to make it faster and save resources
while True:
    try: # try/rxcept saves resource actually
        search = input().strip()
        if len(search)<1: break #-- not used when you do while, try/except
        if search in dic:
            print(search+"="+dic.get(search))
        else: print("Not found")
    except: break
