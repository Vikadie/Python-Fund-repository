month = input().lower()  # "march", "april", "may", "june", "july", "august"
hours_spent = int(input())
people_in_group = int(input())
day_or_night = input().lower()  # "day","night"

price = 0
if month == "march" or month == "april" or month == "may":
    if day_or_night == "day":
        price = 10.5
    else:
        price = 8.4
elif month == "june" or month == "july" or month == "august":
    if day_or_night == "day":
        price = 12.6
    else:
        price = 10.2

if people_in_group >= 4:
    price *= 0.9

if hours_spent >= 5:
    price *= 0.5

total_cost = price * hours_spent * people_in_group

print(f'Price per person for one hour: {price:.2f}')
print(f'Total cost of the visit: {total_cost:.2f}')