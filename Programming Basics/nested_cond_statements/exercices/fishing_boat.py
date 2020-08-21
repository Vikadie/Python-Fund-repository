budget = int(input())
season = input()
fishermen = int(input())

if season == 'Spring':
    price = 3000
elif season == 'Summer' or season == 'Autumn':
    price = 4200
else:
    price = 2600

if fishermen % 2 == 0 and season != 'Autumn':
    if fishermen <= 6:
        price *= 0.9 * 0.95
    elif fishermen <= 11:
        price *= 0.85 * 0.95
    else:
        price *= 0.75 * 0.95
else:
    if fishermen <= 6:
        price *= 0.9
    elif fishermen <= 11:
        price *= 0.85
    else:
        price *= 0.75

if budget >= price:
    print(f'Yes! You have {(budget - price):.2f} leva left.')
else:
    print(f'Not enough money! You need {(price - budget):.2f} leva.')