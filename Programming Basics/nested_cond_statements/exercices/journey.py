budget = float(input())
summer_or_winter = input().lower()

place, type = '', ''
price = budget
if price <= 100:
    place = 'Bulgaria'
    if summer_or_winter == 'summer':
        price *= 0.3
        type = 'Camp'
    else:
        price *= 0.7
        type = 'Hotel'
elif price <= 1000:
    place = 'Balkans'
    if summer_or_winter == 'summer':
        price *= 0.4
        type = 'Camp'
    else:
        price *= 0.8
        type = 'Hotel'
else:
    place = 'Europe'
    type = 'Hotel'
    price *= 0.9

print(f'Somewhere in {place}')
print(f'{type} - {price:.2f}')