q = int(input())
days = int(input())

ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

count, cost, spirit = 0, 0, 0

for i in range(days):
    count += 1
    if count % 11 == 0:
        q += 2
    if count % 2 == 0:
        cost += ornament_set*q
        spirit += 5
    if count % 3 == 0:
        cost += tree_skirt*q
        cost += tree_garlands*q
        spirit += 13
    if count % 5 == 0:
        cost += tree_lights*q
        spirit += 17
        if count % 3 == 0:
            spirit += 30
    if count % 10 == 0:
        spirit -= 20
        cost += tree_skirt
        cost += tree_lights
        cost += tree_garlands
        if count == days:
            spirit -= 30

print(f"Total cost: {cost}")
print("Total spirit:", spirit)