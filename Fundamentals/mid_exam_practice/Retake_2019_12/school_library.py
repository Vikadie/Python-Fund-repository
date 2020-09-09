shelf_with_books = input().split('&')

commands = input()

while commands != 'Done':
    command = commands.split(' | ')
    if command[0] == 'Add Book' and command[1] not in shelf_with_books:
        shelf_with_books.insert(0, command[1])
    elif command[0] == 'Insert Book':
        shelf_with_books.append(command[1])
    elif command[0] == 'Check Book':
        index = int(command[1])
        if 0 <= index < len(shelf_with_books):
            print(shelf_with_books[index])
    elif command[1] in shelf_with_books:

        if command[0] == 'Take Book':
            shelf_with_books.remove(command[1])
        elif command[0] == 'Swap Books':
            if command[2] not in shelf_with_books:
                commands = input()
                continue
            index_1 = shelf_with_books.index(command[1])
            index_2 = shelf_with_books.index(command[2])
            shelf_with_books[index_1], shelf_with_books[index_2] = shelf_with_books[index_2], shelf_with_books[index_1]

    commands = input()

print(', '.join(shelf_with_books))