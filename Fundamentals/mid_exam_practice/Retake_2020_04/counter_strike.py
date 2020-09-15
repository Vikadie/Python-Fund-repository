init_energy = int(input())
distance_to_reach_enemy = input()

stop = 0
won_count = 0
while distance_to_reach_enemy != "End of battle":
    energy = int(distance_to_reach_enemy)
    if init_energy >= energy:
        won_count += 1
        init_energy -= energy
        if won_count % 3 == 0:
            init_energy += won_count
    else:
        print(f"Not enough energy! Game ends with {won_count} won battles and {init_energy} energy")
        stop = 1
        break

    distance_to_reach_enemy = input()

if not stop:
    print(f"Won battles: {won_count}. Energy left: {init_energy}")