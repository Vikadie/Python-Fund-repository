entry = int(input())

first = entry % 10
second = (entry // 10) % 10
third = ((entry // 10) // 10)

# print(entry, first, second, third)

for f in range(1, first + 1):
    for s in range(1, second + 1):
        for t in range(1, third + 1):
            print(f'{f} * {s} * {t} = {f * s * t};')