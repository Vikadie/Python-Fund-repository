username = input()

commands = input()

while commands != 'Sign up':
    command, *args = commands.split()

    if command == 'Case':
        if args[0] == 'upper':
            username = username.upper()
        else:
            username = username.lower()
        print(username)
    elif command == 'Reverse':
        start_index, end_index = int(args[0]), int(args[1])
        if 0 <= start_index < len(username) and 0 <= end_index < len(username):
            to_print = username[start_index: end_index + 1]
            print(to_print[::-1])
    elif command == 'Cut':
        substring = args[0]
        if substring in username:
            username = username.replace(substring, '')
            print(username)
        else:
            print(f"The word {username} doesn't contain {substring}.")
    elif command == 'Replace':
        char = args[0]
        if char in username:
            username = username.replace(char, '*')
            print(username)
    elif command == 'Check':
        char = args[0]
        if char in username:
            print("Valid")
        else:
            print(f"Your username must contain {char}.")

    commands = input()