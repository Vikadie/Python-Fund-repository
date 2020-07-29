film_name = ''
standard_ticket = 0
student_ticket = 0
kid_ticket = 0
total_tickets = 0

while True:
    film_name = input()
    if film_name == 'Finish': break
    free_places = int(input())
    places = free_places
    tickets = 0

    while places > 0:
        ticket_type = input().lower()
        if ticket_type == 'end':
            break
        tickets += 1
        places -= 1

        if ticket_type == 'standard':
            standard_ticket += 1
        elif ticket_type == 'student':
            student_ticket += 1
        elif ticket_type == 'kid':
            kid_ticket += 1

    print(f'{film_name} - {(100 * tickets / free_places):.2f}% full.')
    total_tickets += tickets

print(f'Total tickets: {total_tickets}')
print(f'{(100 * student_ticket / total_tickets):.2f}% student tickets.')
print(f'{(100 * standard_ticket / total_tickets):.2f}% standard tickets.')
print(f'{(100 * kid_ticket / total_tickets):.2f}% kids tickets.')