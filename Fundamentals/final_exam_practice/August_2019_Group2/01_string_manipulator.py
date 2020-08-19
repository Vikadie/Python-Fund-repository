str = input()

commands = input()

while commands != 'Done':
    if commands == 'Uppercase':
        str = str.upper()
        print(str)
    else:
        command, *args = commands.split()
        if command == 'Change':
            char, replacement = args
            if char in str:
                str = str.replace(char, replacement)
                print(str)
        elif command == 'Includes':
            substring = args[0]
            print("True") if substring in str else print("False")
        elif command == 'End':
            substring = args[0]
            print("True") if str.endswith(substring) else print("False")
        elif command == 'FindIndex':
            char = args[0]
            index = str.find(char)
            if index != -1:
                print(index)
        elif command == 'Cut':
            start_index, length = int(args[0]), int(args[1])
            str = str[start_index: start_index + length]
            print(str)

    commands = input()