tickets_list = input().split(',')


def check_size(size, symbol):
    max_count, count = 0, 0
    flag_repeated = False
    for char_index in range(len(size)):
        if size[char_index] == symbol:
            if not flag_repeated:
                count = 1
                flag_repeated = True
            else:
                count += 1
            if count > max_count:
                max_count = count
        else:
            flag_repeated = False
            count = 0
    return max_count


def check_ticket(ticket_size1, ticket_size2):
    match_length = 0
    match_symbol = None
    for symbol in ['@', '#', '$', '^']:
        count1 = check_size(ticket_size1, symbol)
        count2 = check_size(ticket_size2, symbol)
        count = min(count1, count2)

        if count > match_length:
            match_length = count
            match_symbol = symbol

    return match_length, match_symbol


for ticket in tickets_list:
    ticket = ticket.strip()
    if len(ticket) != 20:
        print("invalid ticket")
        continue

    ticket_size_1 = ticket[0: 10]
    ticket_size_2 = ticket[10: 20]

    winning_symbols, match_symbol = check_ticket(ticket_size_1, ticket_size_2)

    if winning_symbols < 6:
        print(f'ticket "{ticket}" - no match')
    elif 6 <= winning_symbols <= 9:
        print(f'ticket "{ticket}" - {winning_symbols}{match_symbol}')
    elif winning_symbols == 10:
        print(f'ticket "{ticket}" - {winning_symbols}{match_symbol} Jackpot!')
