line = input()

d = dict() # people: [health, energy]
while line != 'Results':
    command, *args = line.split(':')
    if command == 'Add':
        person_name, health, energy = args[0], int(args[1]), int(args[2])
        if person_name in d:
            d[person_name][0] += health
        else:
            d[person_name] = [health, energy]
    elif command == 'Attack':
        attacker, defender, damage = args[0], args[1], int(args[2])
        if attacker in d and defender in d:
            d[defender][0] -= damage
            d[attacker][1] -= 1
            if d[defender][0] <= 0:
                del d[defender]
                print(f"{defender} was disqualified!")
            if d[attacker][1] == 0:
                del d[attacker]
                print(f"{attacker} was disqualified!")
    elif command == 'Delete':
        username = args[0]
        if username == 'All':
            d.clear()
        elif username in d:
            del d[username]

    line = input()

print(f"People count: {len(d)}")
d_ordered = dict(sorted(d.items(), key= lambda x: (-x[1][0], x[0])))
for person, data in d_ordered.items():
    print(f"{person} - {data[0]} - {data[1]}")