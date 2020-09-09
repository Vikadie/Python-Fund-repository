gift_list = input().split()

commands = input()

while commands != "No Money":
    command, tokens = commands.split(' ', 1)
    if command == 'OutOfStock':
        if tokens in gift_list:
            for i in range(gift_list.count(tokens)):
                gift_list[gift_list.index(tokens)] = 'None'
    elif command == 'Required':
        tokens = tokens.split()
        gift, index = tokens[0], int(tokens[1])
        if 0 <= index < len(gift_list):
            gift_list[index] = gift
    elif command == 'JustInCase':
        gift_list[-1] = tokens

    commands = input()

[print(gift, end=' ') for gift in gift_list if gift != 'None']