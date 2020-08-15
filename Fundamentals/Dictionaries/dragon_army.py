N = int(input())

statistics = dict()
for _ in range(N):
    type, name, damage, health, armor = input().split()

    if damage == 'null':
        damage = 45
    else:
        damage = int(damage)

    if health == 'null':
        health = 250
    else:
        health = int(health)

    if armor == 'null':
        armor = 10
    else:
        armor = int(armor)

    if type not in statistics:
        temp = dict()
        temp[name] = [damage, health, armor]
        statistics[type] = temp

    statistics[type][name] = [damage, health, armor]

for key in statistics.keys():
    avg_damage = sum([x[0] for k, x in statistics[key].items()])/len(statistics[key])
    avg_health = sum([x[1] for k, x in statistics[key].items()])/len(statistics[key])
    avg_armor = sum([x[2] for k, x in statistics[key].items()])/len(statistics[key])
    print(f"{key}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})")
    sorted_stats = dict(sorted(statistics[key].items(), key=lambda k: k[0]))
    for k, v in sorted_stats.items():
        print(f"-{k} -> damage: {v[0]}, health: {v[1]}, armor: {v[2]}")