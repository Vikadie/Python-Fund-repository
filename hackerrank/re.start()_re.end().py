"""
aaadaa
aa
"""

import re

S = input()
k = re.compile(input())

m = k.search(S)
if not m:
    print("(-1, -1)")
while m:
    print(f'({m.start()}, {m.end() - 1})')
    m = k.search(S, m.start() + 1)
