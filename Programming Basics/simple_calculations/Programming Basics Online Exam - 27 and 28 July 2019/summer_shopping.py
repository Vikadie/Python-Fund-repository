budget = int(input())
towel = float(input())
discount = float(input()) / 100

# article's prices
umbrella = towel * 2/3
flip_flop = 0.75 * umbrella
beach_bag = (towel + flip_flop) / 3

total = (towel + umbrella + beach_bag + flip_flop) * (1 - discount)

if budget >= total:
    print(f"Annie's sum is {total:.2f} lv. She has {budget - total :.2f} lv. left.")
else:
    print(f"Annie's sum is {total:.2f} lv. She needs {total - budget :.2f} lv. more.")