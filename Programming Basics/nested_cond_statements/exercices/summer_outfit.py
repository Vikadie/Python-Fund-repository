degrees = int(input())
daytime = input()

Outfit = ''
Shoes = ''
if 10 <= degrees <= 18:
    if daytime == 'Morning':
        Outfit = 'Sweatshirt'
        Shoes = 'Sneakers'
    else:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
elif 18 < degrees <= 24:
    if daytime == 'Afternoon':
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
    else:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
elif degrees > 24:
    if daytime == 'Morning':
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
    elif daytime == 'Afternoon':
        Outfit = 'Swim Suit'
        Shoes = 'Barefoot'
    else:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'

print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")