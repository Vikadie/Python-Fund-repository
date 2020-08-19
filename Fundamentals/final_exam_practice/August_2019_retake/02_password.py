import re

n = int(input())

pattern = r'^(.+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<(\1)$'
for _ in range(n):
    password = input()

    x = re.findall(pattern, password)

    if x:
        print(f"Password: {x[0][1] + x[0][2] + x[0][3] + x[0][4]}")
    else:
        print("Try another password!")