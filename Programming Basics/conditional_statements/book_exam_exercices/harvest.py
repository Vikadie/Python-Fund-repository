from math import floor
from math import ceil

m2_vine = 0.4 * int(input())
kg_grape = float(input()) # kg grape from 1 m2 vine
needed_l_wine = int(input())
workers = int(input())

l_wine = kg_grape / 2.5 * m2_vine

if l_wine < needed_l_wine:
    print(f'It will be a tough winter! More {floor(needed_l_wine - l_wine)} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {floor(l_wine)} liters.')
    print(f'{ceil(l_wine - needed_l_wine)} liters left -> {ceil((l_wine- needed_l_wine)/workers)} liters per person.')