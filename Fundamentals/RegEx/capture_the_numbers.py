import re

inp_line = input()

while inp_line:
    x = re.findall('\d+',inp_line)
    if x != []:
        print(*x, end=" ")

    inp_line = input()