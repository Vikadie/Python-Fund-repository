from math import ceil

sushi_type = input()  #  "sashimi", "maki", "uramaki", "temaki"
restaurant_name = input()  # "Sushi Zone", "Sushi Time", "Sushi Bar", "Asian Pub"
portions = int(input())
order_for_home = input()
restaurant_name_correct = True

if restaurant_name == "Sushi Zone":
    if sushi_type == "sashimi":
        price = 4.99
    elif sushi_type == "maki":
        price = 5.29
    elif sushi_type == "uramaki":
        price = 5.99
    elif sushi_type == "temaki":
        price = 4.29
elif restaurant_name == "Sushi Time":
    if sushi_type == "sashimi":
        price = 5.49
    elif sushi_type == "maki":
        price = 4.69
    elif sushi_type == "uramaki":
        price = 4.49
    elif sushi_type == "temaki":
        price = 5.19
elif restaurant_name == "Sushi Bar":
    if sushi_type == "sashimi":
        price = 5.25
    elif sushi_type == "maki":
        price = 5.55
    elif sushi_type == "uramaki":
        price = 6.25
    elif sushi_type == "temaki":
        price = 4.75
elif restaurant_name == "Asian Pub":
    if sushi_type == "sashimi":
        price = 4.5
    elif sushi_type == "maki":
        price = 4.8
    elif sushi_type == "uramaki":
        price = 5.5
    elif sushi_type == "temaki":
        price = 5.5
else:
    print(f'{restaurant_name} is invalid restaurant!')
    restaurant_name_correct = False

if restaurant_name_correct:
    total_price = price * portions

    if order_for_home == 'Y':
        total_price *= 1.2

    print(f'Total price: {ceil(total_price)} lv.')