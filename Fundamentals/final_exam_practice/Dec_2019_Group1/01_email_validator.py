email = input()

commands = input()

while commands != 'Complete':
    if commands == 'GetUsername':
        if '@' in email:
            print(email.split('@')[0])
        else:
            print(f"The email {email} doesn't contain the @ symbol.")
    elif commands == 'Encrypt':
        ascii_list = [str(ord(ch)) for ch in email]
        print(' '.join(ascii_list))
    else:
        command1, command2 = commands.split()
        if command1 == 'Make':
            if command2 == 'Upper':
                email = email.upper()
            elif command2 == 'Lower':
                email = email.lower()
            print(email)
        elif command1 == 'GetDomain':
            count = int(command2)
            print(email[-count:])
        elif command1 == 'Replace':
            char = command2
            email = email.replace(command2, '-')
            print(email)

    commands = input()
