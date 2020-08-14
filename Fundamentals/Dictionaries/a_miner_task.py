resource = input()

d = dict()
while resource != 'stop':
    quantity = int(input())
    d[resource] = d.get(resource, 0) + quantity

    resource = input()

for r, q in d.items():
    print(f'{r} -> {q}')