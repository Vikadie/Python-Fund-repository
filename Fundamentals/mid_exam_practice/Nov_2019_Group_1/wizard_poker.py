all_cards = input().split(':')

commands = input()

new_deck = []
while commands != 'Ready':
    command, tokens = commands.split(' ', 1)
    if command == 'Add':
        if tokens in all_cards:
            new_deck.append(tokens)
        else:
            print('Card not found.')
    elif command == 'Insert':
        card_name, index = tokens.split()
        index = int(index)
        if 0 <= index < len(new_deck) and card_name in all_cards:
            new_deck.insert(index, card_name)
        else:
            print("Error!")
    elif command == 'Remove':
        if tokens in new_deck:
            new_deck.remove(tokens)
        else:
            print("Card not found.")
    elif command == 'Swap':
        card1, card2 = tokens.split()
        if card1 in new_deck and card2 in new_deck:
            index1 = new_deck.index(card1)
            index2 = new_deck.index(card2)
            new_deck[index1], new_deck[index2] = new_deck[index2], new_deck[index1]
    elif command == 'Shuffle':
        new_deck = new_deck[::-1]

    commands = input()

print(' '.join(new_deck))