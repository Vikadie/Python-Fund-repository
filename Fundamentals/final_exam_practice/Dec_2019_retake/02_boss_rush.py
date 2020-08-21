import re

n = int(input())

for _ in range(n):
    boss_name = input()

    pattern = r'\|([A-Z]{4,})\|:#([A-Za-z]+\s[A-Za-z]+)#'

    x = re.findall(pattern, boss_name)

    if x:
        print(f"{x[0][0]}, The {x[0][1]}\n>> Strength: {len(x[0][0])}\n>> Armour: {len(x[0][1])}")
    else:
        print("Access denied!")