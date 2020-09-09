pirate_ship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
max_health = int(input())

commands = input()
game_over = 0
while commands != 'Retire':
    tokens = commands.split()
    if tokens[0] == 'Fire':
        index, damage = int(tokens[1]), int(tokens[2])
        if 0 <= index < len(warship):
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                game_over = 1
                break
    elif tokens[0] == 'Defend':
        startIndex, endIndex, damage = int(tokens[1]), int(tokens[2]), int(tokens[3])
        if 0<= startIndex < len(pirate_ship) and 0<= endIndex < len(pirate_ship):
            for i in range(startIndex, endIndex + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    game_over = 1
                    break
            if game_over: break
    elif tokens[0] == 'Repair':
        index, health = int(tokens[1]), int(tokens[2])
        if 0 <= index < len(pirate_ship):
            pirate_ship[index] += health
            if pirate_ship[index] > max_health:
                pirate_ship[index] = max_health
    elif tokens[0] == 'Status':
        check_level = max_health * 0.2
        count = 0
        for section in pirate_ship:
            if section < check_level:
                count += 1
        print(f"{count} sections need repair.")

    commands = input()

if not game_over:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")