inp = input()

d = dict()
for char in inp:
    if char != ' ':
        d[char] = d.get(char, 0) + 1

for key, value in d.items():
    print(f'{key} -> {value}')