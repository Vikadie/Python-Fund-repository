line = input()

menu = dict()
list_unliked = list()
while line != "Stop":
    commands = line.split('-')
    command, guest, meal = commands[0], commands[1], commands[2]
    if command == 'Like':
        if guest in menu:
            if meal not in menu[guest]:
                menu[guest].append(meal)
        else:
            menu[guest] = [meal]
    elif command == 'Unlike':
        if guest in menu:
            if meal in menu[guest]:
                menu[guest].remove(meal)
                list_unliked.append(meal)
                print(f"{guest} doesn't like the {meal}.")
            else:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            print(f"{guest} is not at the party.")

    line = input()

sorted_menu = dict(sorted(menu.items(), key=lambda x: (-len(x[1]), x[0])))

for guest, meals in sorted_menu.items():
    print(f"{guest}: {', '.join(meals)}")
print(f"Unliked meals: {len(list_unliked)}")