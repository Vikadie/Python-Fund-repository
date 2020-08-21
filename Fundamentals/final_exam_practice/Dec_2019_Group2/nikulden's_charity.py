str = input()

decrypting_commmands = input()

while decrypting_commmands != 'Finish':
    commands = decrypting_commmands.split()

    if commands[0] == 'Replace':
        current_char, new_char = commands[1], commands[2]
        if current_char in str:
            str = str.replace(current_char, new_char)
            print(str)
    elif commands[0] == 'Cut':
        start_index, end_index = int(commands[1]), int(commands[2])
        if 0 <= start_index < len(str) and 0 <= end_index < len(str):
            str = str[:start_index] + str[end_index + 1:]
            print(str)
        else:
            print("Invalid indexes!")
    elif commands[0] == 'Make':
        if commands[1] == 'Upper':
            str = str.upper()
        elif commands[1] == 'Lower':
            str = str.lower()
        print(str)
    elif commands[0] == 'Check':
        string = commands[1]
        if string in str:
            print(f"Message contains {string}")
        else:
            print(f"Message doesn't contain {string}")
    elif commands[0] == 'Sum':
        start_index, end_index = int(commands[1]), int(commands[2])
        ssum = 0
        if 0 <= start_index < len(str) and 0 <= end_index < len(str):
            for i in range(start_index, end_index + 1):
                ssum += ord(str[i])
            print(ssum)
        else:
            print("Invalid indexes!")

    decrypting_commmands = input()