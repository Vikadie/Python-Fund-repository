health = 100
bitcoins = 0

dungeons_rooms = input().split('|')
game_over = False
for room_number in range(len(dungeons_rooms)):
    monster_or_help , power = dungeons_rooms[room_number].split()
    power = int(power)
    if monster_or_help == "potion":
        need_for_heal = 100 - health
        if power <= need_for_heal:
            health += power
            print(f"You healed for {power} hp.")
        else:
            health = 100
            print(f"You healed for {need_for_heal} hp.")
        print(f"Current health: {health} hp.")

    elif monster_or_help == "chest":
        print(f"You found {power} bitcoins.")
        bitcoins += power
    else:
        health -= power
        if health > 0:
            print(f"You slayed {monster_or_help}.")
        else:
            print(f"You died! Killed by {monster_or_help}.")
            game_over = True
            print(f"Best room: {room_number + 1}")
            break

if not game_over:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")
