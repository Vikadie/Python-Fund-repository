msg = input()

instruction = input()

while instruction != "Reveal":
    commands = instruction.split(":|:")
    if commands[0] == 'InsertSpace':
        index_empty_space = int(commands[1])
        msg = msg[:index_empty_space] + ' ' + msg[index_empty_space:]
        print(msg)
    elif commands[0] == 'Reverse':
        substring = commands[1]
        if substring in msg:
            msg = msg.replace(substring, '', 1)
            msg += substring[::-1]
            print(msg)
        else:
            print("error")
    elif commands[0] == 'ChangeAll':
        substring = commands[1]
        replacement = commands[2]
        msg = msg.replace(substring, replacement)
        print(msg)

    instruction = input()

print(f"You have a new text message: {msg}")
