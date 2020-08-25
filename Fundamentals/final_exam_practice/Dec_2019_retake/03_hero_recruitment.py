line = input()

heroes = dict()
while line != 'End':
    commands = line.split()
    if commands[0] == 'Enroll':
        hero_name = commands[1]
        if hero_name in heroes:
            print(f"{hero_name} is already enrolled.")
        else:
            heroes[hero_name] = []
    elif commands[0] == 'Learn':
        hero_name, spell_name = commands[1], commands[2]
        if hero_name in heroes:
            if spell_name in heroes[hero_name]:
                print(f"{hero_name} has already learnt {spell_name}.")
            else:
                heroes[hero_name].append(spell_name)
        else:
            print(f"{hero_name} doesn't exist.")

    elif commands[0] == 'Unlearn':
        hero_name, spell_name = commands[1], commands[2]
        if hero_name in heroes:
            if spell_name in heroes[hero_name]:
                heroes[hero_name].remove(spell_name)
            else:
                print(f"{hero_name} doesn't know {spell_name}.")
        else:
            print(f"{hero_name} doesn't exist.")

    line = input()

heroes_sorted = dict(sorted(heroes.items(), key=lambda x: (-len(x[1]), x[0])))

print("Heroes:")
for hero, spell_list in heroes_sorted.items():
    print(f"== {hero}: {', '.join(heroes_sorted[hero])}")