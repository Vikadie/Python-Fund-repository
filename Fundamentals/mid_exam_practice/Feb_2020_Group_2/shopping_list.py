init_shopping_list = input().split('!')

commands = input()
while commands != "Go Shopping!":
    command = commands.split()
    if command[0] == 'Urgent' and command[1] not in init_shopping_list:
        init_shopping_list.insert(0, command[1])
    elif command[1] in init_shopping_list:
        if command[0] == 'Unnecessary':
            init_shopping_list.remove(command[1])
        elif command[0] == 'Correct':
            index_item_to_replace = init_shopping_list.index(command[1])
            init_shopping_list[index_item_to_replace] = command[2]
        elif command[0] == 'Rearrange':
            init_shopping_list.remove(command[1])
            init_shopping_list.append(command[1])

    commands = input()

print(', '.join(init_shopping_list))