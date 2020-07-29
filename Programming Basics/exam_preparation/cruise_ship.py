cruise_type = input()
cabin_type = input().lower()
nights = int(input())

if cruise_type == 'Mediterranean':
    if cabin_type == 'standard cabin':
        price = 27.5
    elif cabin_type == 'cabin with balcony':
        price = 30.2
    elif cabin_type == 'apartment':
        price = 40.5
elif cruise_type == 'Adriatic':
    if cabin_type == 'standard cabin':
        price = 22.99
    elif cabin_type == 'cabin with balcony':
        price = 25
    elif cabin_type == 'apartment':
        price = 34.99
elif cruise_type == 'Aegean':
    if cabin_type == 'standard cabin':
        price = 23
    elif cabin_type == 'cabin with balcony':
        price = 26.6
    elif cabin_type == 'apartment':
        price = 39.8
# повече от 7 нощувки има 25% отстъпка.
if nights > 7:
    amount = 0.75 * price * nights * 4
else:
    amount = price * nights * 4

print(f"Annie's holiday in the {cruise_type} sea costs {amount:.2f} lv.")
