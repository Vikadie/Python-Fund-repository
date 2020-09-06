hours_per_task = list(map(int, input().split()))

commands = input()

while commands != 'End':
    command, tokens = commands.split(' ', 1)
    if command == 'Complete':
        index = int(tokens)
        if 0 <= index < len(hours_per_task):
            hours_per_task[index] = 0
    elif command == 'Change':
        index, time = tuple(map(int, tokens.split()))
        if 0 <= index < len(hours_per_task):
            hours_per_task[index] = time
    elif command == 'Drop':
        index = int(tokens)
        if 0 <= index < len(hours_per_task):
            hours_per_task[index] = -1
    elif command == 'Count':
        count = 0
        if tokens == 'Completed':
            for i in hours_per_task:
                if i == 0:
                    count += 1
        elif tokens == 'Incomplete':
            for i in hours_per_task:
                if i > 0:
                    count += 1
        elif tokens == 'Dropped':
            for i in hours_per_task:
                if i == -1:
                    count += 1
        print(count)

    commands = input()

for i in hours_per_task:
    if i > 0:
        print(i, end= ' ')
