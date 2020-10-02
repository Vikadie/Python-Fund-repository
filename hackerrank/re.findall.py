import re

inp = input().strip()

pattern = r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})[qwrtypsdfghjklzxcvbnm]'
# (?<=...) positive lookbehind is needed in this case as it should not miss 'ae' in 'abaabaebaibaoe' for instance
m = re.findall(pattern, inp, re.IGNORECASE)

# [print(e) if m else print(-1) for e in m]
if m:
    for e in m:
        print(e)
else:
    print(-1)