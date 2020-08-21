cruise = input()
cabin = input()
nights = int(input())

if cruise == "Mediterranean":
    if cabin == "standard cabin":
        price = 27.5
    elif cabin == "cabin with balcony":
        price = 30.2
    elif cabin == "apartment":
        price = 40.5
elif cruise == "Adriatic":
    if cabin == "standard cabin":
        price = 22.99
    elif cabin == "cabin with balcony":
        price = 25
    elif cabin == "apartment":
        price = 34.99
elif cruise == "Aegean":
    if cabin == "standard cabin":
        price = 23
    elif cabin == "cabin with balcony":
        price = 26.6
    elif cabin == "apartment":
        price = 39.8
else:
    print(f"You have inserted wrong cruising company {cruise}.")

if 0 < nights <= 7:
    amount = 4 * price * nights
else:
    amount = 4 * price * nights * 0.75

print(f"Annie's holiday in the {cruise} sea costs {amount:.2f} lv.")