pirate_ship = list(map(int, input().split(">")))
warship = list(map(int, input().split(">")))
max_health_capacity = int(input())

commands = input()

stop = 0
while commands != "Retire":
    command = commands.split()

    if command[0] == "Fire": # pirate ship attacks the warship
        index, damage = int(command[1]), int(command[2])
        if 0 <= index < len(warship) :
            if damage < warship[index]:
                warship[index] -= damage
            else:
                print("You won! The enemy ship has sunken.")
                stop = 1
                break
        # [print(x, end=" ") for x in warship]

    elif command[0] == "Defend":
        start_index, end_index, damage = int(command[1]), int(command[2]), int(command[3])
        if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship) and start_index < end_index:
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    stop = 1
                    print("You lost! The pirate ship has sunken.")
                    break
        if stop:
            break
        # [print(x, end=" ") for x in pirate_ship]

    elif command[0] == "Repair":
        index, health = int(command[1]), int(command[2])
        if 0 <= index < len(pirate_ship):
            pirate_ship[index] += health
            if pirate_ship[index] > max_health_capacity:
                pirate_ship[index] = max_health_capacity
        # [print(x, end=" ") for x in pirate_ship]

    elif command[0] == "Status":
        section_count_for_repair = 0
        for health_status_per_section in pirate_ship:
            if health_status_per_section < max_health_capacity * 0.2:
                section_count_for_repair += 1
        print(f"{section_count_for_repair} sections need repair.")
        # [print(x, end=" ") for x in pirate_ship]

    commands = input()

if not stop:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")