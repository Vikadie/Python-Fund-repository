import re

line = input()

pattern = "(www\.[A-Za-z-0-9]+\.[\.a-z]+[\.a-z-0-9]+)"
y = []
while line:
    x = re.findall(pattern, line)
    if x:
        y+= x

    line = input()

for x in y:
    print(x)