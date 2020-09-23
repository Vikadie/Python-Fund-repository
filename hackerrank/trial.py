import re

n = int(input())

pattern = r'([-\+]?[\d]*[.][\d]*)'

for _ in range(n):
    y = input()
    x = re.fullmatch(pattern, y)

    if x and len(y) == len(x[0]):
            print("True")
            continue
    print("False")
