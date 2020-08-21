skill_to_decipher = input()

commands = input()

while commands != 'For Azeroth':
    if commands == 'GladiatorStance':
        skill_to_decipher = skill_to_decipher.upper()
        print(skill_to_decipher)
    elif commands == 'DefensiveStance':
        skill_to_decipher = skill_to_decipher.lower()
        print(skill_to_decipher)
    else:
        command = commands.split()
        if command[0] == 'Dispel':
            index, letter = int(command[1]), command[2]
            if index < 0 or index >= len(skill_to_decipher):
                print("Dispel too weak.")
            else:
                skill_to_decipher = skill_to_decipher[: index] + letter + skill_to_decipher[index + 1:]
                print("Success!")
        elif command[1] == 'Change':
            substr1, substr2 = command[2], command[3]
            if substr1 in skill_to_decipher:
                skill_to_decipher = skill_to_decipher.replace(substr1, substr2)
                print(skill_to_decipher)
        elif command[1] == 'Remove':
            substring = command[2]
            if substring in skill_to_decipher:
                skill_to_decipher = skill_to_decipher.replace(substring, '')
                print(skill_to_decipher)
        else:
            print("Command doesn't exist!")

    commands = input()