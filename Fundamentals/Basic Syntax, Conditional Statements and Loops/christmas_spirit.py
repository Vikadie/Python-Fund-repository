allowed_q = int(input())
days_left = int(input())

ornament = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

cost, spirit = 0, 0

for days in range(1, days_left + 1):
    if days % 11 == 0:
        allowed_q += 2
    if days % 2 == 0:
        cost += ornament * allowed_q
        spirit += 5
    if days % 3 == 0:
        cost += tree_skirt * allowed_q
        cost += tree_garlands * allowed_q
        spirit += 13
    if days % 5 == 0:
        cost += tree_lights * allowed_q
        spirit += 17
        if days % 3 == 0:
            spirit += 30
    if days % 10 == 0:
        spirit -= 20
        cost += (tree_skirt + tree_lights + tree_garlands)
        if days == days_left:
            spirit -= 30

print(f"Total cost: {cost}")
print(f"Total spirit: {spirit}")