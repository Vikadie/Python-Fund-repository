str = input()

commands = input()

while commands != 'End':
    if commands == 'Lowercase':
        str = str.lower()
        print(str)
    else:
        command, *args = commands.split()
        if command == 'Translate':
            char, replacement = args
            if char in str:
                str = str.replace(char, replacement)
                print(str)
        elif command == 'Includes':
            str1 = args[0]
            print(True) if str1 in str else print(False)
        elif command == 'Start':
            str1 = args[0]
            print(True) if str.startswith(str1) else print(False)
        elif command == 'FindIndex':
            char = args[0]
            if char in str:
                print(str.rfind(char))
        elif command == 'Remove':
            startIndex, count = int(args[0]), int(args[1])
            str = str[:startIndex] + str[startIndex + count:]
            print(str)
            # hello 1 3 = h + o
    commands = input()