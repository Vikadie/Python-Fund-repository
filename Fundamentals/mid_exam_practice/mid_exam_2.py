#Array modifier
input_list = list(map(int, input().split()))

commands = input()

while commands != 'end':
    if commands == 'decrease':
        for index in range(len(input_list)):
            input_list[index] -= 1
    else:
        command, index1, index2 = commands.split()
        index_1 = int(index1)
        index_2 = int(index2)
        if command == 'swap':
            input_list[index_1], input_list[index_2] = input_list[index_2], input_list[index_1]
        elif command == 'multiply':
            input_list[index_1] *= input_list[index_2]

    commands = input()

output = [str(e) for e in input_list]
print(', '.join(output))
