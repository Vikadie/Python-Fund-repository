raw_activation_key = input()

instructions = input()

while instructions != 'Generate':
    commands = instructions.split('>>>')
    if commands[0] == 'Contains':
        substring = commands[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif commands[0] == 'Flip':
        upper_lower, start_index, end_index = commands[1], int(commands[2]), int(commands[3])
        if upper_lower == 'Upper':
            str = raw_activation_key[start_index: end_index].upper()
        else:
            str = raw_activation_key[start_index: end_index].lower()
        raw_activation_key = raw_activation_key[:start_index] + str + raw_activation_key[end_index:]
        print(raw_activation_key)
    elif commands[0] == 'Slice':
        start_index, end_index = int(commands[1]), int(commands[2])
        raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[end_index:]
        print(raw_activation_key)

    instructions = input()

print(f"Your activation key is: {raw_activation_key}")
