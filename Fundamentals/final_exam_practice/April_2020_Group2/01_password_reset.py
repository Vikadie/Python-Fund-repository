pass_txt = input()

commands = input()

while commands != "Done":
    if commands == 'TakeOdd':
        raw_string = ''
        for i in range(1, len(pass_txt), 2):
            raw_string += pass_txt[i]
        print(raw_string)
        pass_txt = raw_string
    else:
        commands = commands.split()
        if commands[0] == 'Cut':
            index, length = int(commands[1]), int(commands[2])
            substring = pass_txt[index: index + length]
            pass_txt = pass_txt.replace(substring, '', 1)
            print(pass_txt)
        elif commands[0] == 'Substitute':
            substring, substitute = commands[1], commands[2]
            if substring in pass_txt:
                pass_txt = pass_txt.replace(substring, substitute)
                print(pass_txt)
            else:
                print("Nothing to replace!")

    commands = input()

print(f"Your password is: {pass_txt}")