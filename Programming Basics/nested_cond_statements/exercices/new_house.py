flower_type = input()  # Rose, Dahlias, Tulips, Narcissus, Gladiolus
flower_num = int(input())
budget = int(input())

flower = flower_type.lower()

price = 0
if flower == 'roses':
    price = 5
    if flower_num > 80:
        price *= 0.9
elif flower == 'dahlias':
    price = 3.8
    if flower_num > 90:
        price *= 0.85
elif flower == 'tulips':
    price = 2.8
    if flower_num > 80:
        price *= 0.85
elif flower == 'narcissus':
    price = 3
    if flower_num < 120:
        price *= 1.15
elif flower == 'gladiolus':
    price = 2.5
    if flower_num < 80:
        price *= 1.2

if price > 0:
    total_price = flower_num * price
else:
    print('invalid input')

if budget >= total_price:
    print(f'Hey, you have a great garden with {flower_num} {flower_type} and {(budget - total_price):.2f} leva left.')
else:
    print(f'Not enough money, you need {(total_price - budget):.2f} leva more.')