inp = input()

d = dict()
while inp != 'no more time':
    username, contest, points_str = inp.split(' -> ')
    points = int(points_str)
    if contest in d:
        if username in d[contest]:
            if points > d[contest][username]:
                d[contest][username] = points
        else:
            d[contest][username] = points
    else:
        user_points_dict = dict()
        user_points_dict[username] = points
        d[contest] = user_points_dict

    inp = input()

for contest in d:
    print(f"{contest}: {len(d[contest])} participants")
    sorted_users = dict(sorted(d[contest].items(), key = lambda x: (-x[1], x[0])))
    count = 1
    for user in sorted_users.keys():
        print(f"{count}. {user} <::> {sorted_users[user]}")
        count += 1

print("Individual standings:")
individual = dict()
for c in d:
    for u, p in d[c].items():
        individual[u] = individual.get(u, 0) + p

sorted_individuals = dict(sorted(individual.items(), key = lambda x: (-x[1], x[0])))
count = 1
for u, p in sorted_individuals.items():
    print(f"{count}. {u} -> {p}")
    count += 1
