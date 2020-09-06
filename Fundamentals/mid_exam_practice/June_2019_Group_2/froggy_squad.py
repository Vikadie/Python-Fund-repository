frogs_names = input().split()

while True:
    commands = input().split()

    if commands[0] == 'Join':
        name = commands[1]
        frogs_names.append(name)
    elif commands[0] == 'Jump':
        name, index = commands[1], int(commands[2])
        if 0 <= index < len(frogs_names):
            frogs_names.insert(index, name)
    elif commands[0] == 'Dive':
        index = int(commands[1])
        if 0 <= index < len(frogs_names):
            del frogs_names[index]
    elif commands[0] == 'First':
        count = int(commands[1])
        if count < len(frogs_names):
            for i in range(count):
                print(frogs_names[i], end=' ')
            print()
        else:
            print(' '.join(frogs_names))
    elif commands[0] == 'Last':
        count = int(commands[1])
        if count < len(frogs_names):
            for i in range(len(frogs_names) - count, len(frogs_names)):
                print(frogs_names[i], end=' ')
            print()
        else:
            print(' '.join(frogs_names))
    elif commands[0] == 'Print':
        print("Frogs:", end =' ')
        if commands[1] == 'Normal':
            print(' '.join(frogs_names))
        else:
            print(' '.join(frogs_names[::-1]))
        break

