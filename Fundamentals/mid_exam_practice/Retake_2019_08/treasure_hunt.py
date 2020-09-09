treasure = input().split('|')

commands = input()

while commands != 'Yohoho!':
    command, tokens = commands.split(' ', 1)
    if command == 'Loot':
        item_list = tokens.split()
        for item in item_list:
            if item not in treasure:
                treasure.insert(0, item)
    else:
        num = int(tokens)
        if command == 'Drop':
            if 0 <= num < len(treasure):
                treasure.append(treasure[num])
                del treasure[num]

        elif command == 'Steal':
            if num >= len(treasure):
                print(', '.join(treasure))
                treasure.clear()
            else:
                print(', '.join(treasure[-num :]))
                for count in range(num):
                    treasure.pop()
    commands = input()

if len(treasure) == 0:
    print("Failed treasure hunt.")
else:
    sum = 0
    for item in treasure:
        sum += len(item)

    gain = sum / len(treasure)
    print(f"Average treasure gain: {gain:.2f} pirate credits.")

