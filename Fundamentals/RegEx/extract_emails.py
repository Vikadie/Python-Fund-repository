import re

line = input()
user = '[A-Za-z0-9]+[-._]?[A-Za-z0-9]+'
host = '[A-Za-z0-9-]+[\.{1}][A-Za-z\.]+'
pattern = fr'\b({user}@{host})\b'


for y in line.split():
    x = re.findall(pattern, y)
    if x:
        print(*x)