days = int(input())
room = input()
rating = input()

price, discount = 0, 0
if room == 'room for one person':
    price = 18
elif room == 'apartment':
    price = 25
    if (days - 1) < 10:
        price *= 0.7
    elif 10 <= (days - 1) <= 15:
        price *= 0.65
    elif (days - 1) > 15:
        price *= 0.5
elif room == 'president apartment':
    price = 35
    if (days - 1) < 10:
        price *= 0.9
    elif 10 <= (days - 1) <= 15:
        price *= 0.85
    elif (days - 1) > 15:
        price *= 0.8

total_amount = (days - 1) * price

if rating == "positive":
    total_amount *= 1.25
elif rating == "negative":
    total_amount *= 0.9

print("%.2f" % total_amount)