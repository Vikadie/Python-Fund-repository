n = int(input())

plants = dict()
for _ in range(n):
    line = input()
    plant, rarity_str = line.split('<->')
    rarity = int(rarity_str)
    if plant in plants:
        plants[plant][0] = rarity
    else:
        plants[plant] = [rarity, []]

commands = input()

while commands != 'Exhibition':
    command, token = commands.split(': ')
    if command == 'Rate':
        plant, rating_str = token.split(' - ')
        rating = int(rating_str)
        if plant in plants:
            plants[plant][1].append(rating)
        else:
            print('error')
    elif command == 'Update':
        plant, new_rarity_str = token.split(' - ')
        new_rarity = int(new_rarity_str)
        if plant in plants:
            plants[plant][0] = new_rarity
        else:
            print('error')
    elif command == 'Reset':
        if token in plants:
            plants[token][1].clear()
        else:
            print('error')

    commands = input()

print("Plants for the exhibition:")
new_plants = {}
for plant in plants.keys():
    if len(plants[plant][1]) == 0:
        avg_rating = 0
    else:
        avg_rating = sum(plants[plant][1])/len(plants[plant][1])
    new_plants[plant] = [plants[plant][0], avg_rating]

plants_sorted = dict(sorted(new_plants.items(), key=lambda x: (-x[1][0], -x[1][1])))

for plant_name, data in plants_sorted.items():
    print(f'- {plant_name}; Rarity: {data[0]}; Rating: {(data[1]):.2f}')