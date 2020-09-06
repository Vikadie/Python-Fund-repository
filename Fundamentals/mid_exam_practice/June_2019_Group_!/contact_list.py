contact_list = input().split()

commands = input().split()

while True:
    if commands[0] == 'Add':
        contact, index = commands[1], int(commands[2])
        if contact in contact_list:
            if 0 <= index < len(contact_list):
                contact_list.insert(index, contact)
        else:
            contact_list.append(contact)
    if commands[0] == 'Remove':
        index = int(commands[1])
        if 0 <= index < len(contact_list):
            del contact_list[index]
    if commands[0] == 'Export':
        start_index, count = int(commands[1]), int(commands[2])
        if 0 <= start_index < len(contact_list):
            if start_index + count + 1 > len(contact_list):
                print(' '.join(contact_list[start_index: ]))
            else:
                print(' '.join(contact_list[start_index : start_index + count]))
    if commands[0] == 'Print':
        print("Contacts:", end=" ")
        if commands[1] == 'Normal':
            print(' '.join(contact_list))
        else:
            print(' '.join(contact_list[::-1]))
        break

    commands = input().split()
