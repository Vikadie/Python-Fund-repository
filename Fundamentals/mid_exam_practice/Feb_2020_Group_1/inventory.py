collecting_items = input().split(', ')

commands = input()
while commands != "Craft!":
    command, item = commands.split(' - ')
    if command == "Collect":
        if item not in collecting_items:
            collecting_items.append(item)
    elif command == "Drop":
        if item in collecting_items:
            collecting_items.remove(item)
    elif command == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in collecting_items:
            collecting_items.insert(collecting_items.index(old_item) + 1, new_item)
    elif command == "Renew":
        if item in collecting_items:
            collecting_items.remove(item)
            collecting_items.append(item)

    commands = input()

print(', '.join(collecting_items))