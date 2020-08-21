age = int(input())
laundry_price = float(input())
toy_price = int(input())

savings = 0
toy_count = 0
for year in range(1, age + 1):
    if year % 2 == 0:
        savings += (year / 2) * 10 - 1
    else:
        toy_count += 1

money_collected = savings + toy_count * toy_price

if laundry_price > money_collected:
    print(f'No! {(laundry_price - money_collected):.2f}')
else:
    print(f'Yes! {(money_collected - laundry_price):.2f}')