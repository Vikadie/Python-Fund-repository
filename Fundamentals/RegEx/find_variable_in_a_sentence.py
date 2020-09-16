import re

pattern = r'\b_([A-Za-z]+)\b'

sstr = input()
x = re.finditer(pattern, sstr)

print(",".join([match[1] for match in x]))
