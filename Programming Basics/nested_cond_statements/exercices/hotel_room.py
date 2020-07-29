month = input().lower()  # May, June, July, August, September или October
nights = int(input())

price_studio, price_app = 0, 0
if month == "may" or month == "october":
    price_studio = 50
    price_app = 65
    if nights > 14:
        price_studio *= 0.7
        price_app *= 0.9
    elif nights > 7:
        price_studio *= 0.95
elif month == "june" or month == "september":
    price_studio = 75.2
    price_app = 68.7
    if nights > 14:
        price_studio *= 0.8
        price_app *= 0.9
elif month == "july" or month == "august":
    price_studio = 76
    price_app = 77
    if nights > 14:
        price_app *= 0.9

print(f'Apartment: {(price_app * nights):.2f} lv.')
print(f'Studio: {(price_studio * nights):.2f} lv.')