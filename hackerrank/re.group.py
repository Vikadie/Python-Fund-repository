import re

inp = input()

pattern = r'([a-zA-Z0-9])\1'
m = re.search(pattern, inp)

print(m.group(1))
print(m.group(0))
print(m.groups())