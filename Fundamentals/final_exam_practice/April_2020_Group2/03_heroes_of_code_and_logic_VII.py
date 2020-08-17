number_of_heroes = int(input())

d = dict()
for _ in range(number_of_heroes):
    hero_name, HP, MP = input().split()
    HP = int(HP)
    MP = int(MP)
    if HP >= 100: HP = 100
    if MP >= 200: MP = 200
    d[hero_name] = [HP, MP]

command = input()

while command != 'End':
    command = command.split(' - ')
    if command[0] == 'CastSpell':
        hero_name, MP_needed, spell_name = command[1], int(command[2]), command[3]
        if hero_name in d:
            if d[hero_name][1] >= MP_needed:
                d[hero_name][1] -= MP_needed
                print(f"{hero_name} has successfully cast {spell_name} and now has {d[hero_name][1]} MP!")
            else:
                print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif command[0] == 'TakeDamage':
        hero_name, damage, attacker = command[1], int(command[2]), command[3]
        if hero_name in d:
            d[hero_name][0] -= damage
            if d[hero_name][0] <= 0:
                del d[hero_name]
                print(f"{hero_name} has been killed by {attacker}!")
            else:
                print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {d[hero_name][0]} HP left!")

    elif command[0] == 'Recharge':
        hero_name, amount = command[1], int(command[2])
        if hero_name in d:
            if d[hero_name][1] + amount > 200:
                amount = 200 - d[hero_name][1]
                d[hero_name][1] = 200
            else:
                d[hero_name][1] += amount
            print(f"{hero_name} recharged for {amount} MP!")
    elif command[0] == 'Heal':
        hero_name, amount = command[1], int(command[2])
        if hero_name in d:
            if d[hero_name][0] + amount > 100:
                amount = 100 - d[hero_name][0]
                d[hero_name][0] = 100
            else:
                d[hero_name][0] += amount
            print(f"{hero_name} healed for {amount} HP!")

    command = input()

d_sorted = dict(sorted(d.items(), key=lambda x: (-x[1][0], x[0])))

for hero, data in d_sorted.items():
    print(f'{hero}\n  HP: {data[0]}\n  MP: {data[1]}')