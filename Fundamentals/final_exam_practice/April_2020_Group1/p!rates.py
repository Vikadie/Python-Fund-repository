str = input()

d = dict()
while str != 'Sail':
    city, population, gold = str.split('||')
    if city in d:
        d[city][0] += int(population)
        d[city][1] += int(gold)
    else:
        d[city] = [int(population), int(gold)]

    str = input()

events = input()

while events != 'End':
    command = events.split('=>')
    if command[0] == 'Plunder':
        town, people, gold = command[1], int(command[2]), int(command[3])
        if town in d:
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
            d[town][0] -= people
            d[town][1] -= gold
            if d[town][0] == 0 or d[town][1] == 0:
                del d[town]
                print(f"{town} has been wiped off the map!")
    elif command[0] == 'Prosper':
        town, gold = command[1], int(command[2])
        if town in d:
            if gold >= 0:
                d[town][1] += gold
                print(f"{gold} gold added to the city treasury. {town} now has {d[town][1]} gold.")
            else:
                print("Gold added cannot be a negative number!")

    events = input()

if len(d) > 0:
    d_sorted = dict(sorted(d.items(), key=lambda x: (-x[1][1], x[0])))
    print(f'Ahoy, Captain! There are {len(d)} wealthy settlements to go to:')
    for town, (people, gold) in d_sorted.items():
        print(f'{town} -> Population: {people} citizens, Gold: {gold} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

