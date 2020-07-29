budget = int(input())
summer_towel = float(input())
discount = int(input()) / 100

sun_umbrella = 2 / 3 * summer_towel
flip_flops = 0.75 * sun_umbrella
summer_bag = 1 / 3 * (flip_flops + summer_towel)

# if > 0: Annie's sum is {общата сума} lv. She has {оставащата сума} lv. left.
# else: Annie's sum is {общата сума} lv. She needs {недостигащата сума} lv. more.

total_amount = (1 - discount) * (summer_towel + sun_umbrella + flip_flops + summer_bag)

if budget >= total_amount:
    print(f"Annie's sum is {total_amount:.2f} lv. She has {(budget - total_amount):.2f} lv. left.")
else:
    print(f"Annie's sum is {total_amount:.2f} lv. She needs {(total_amount - budget):.2f} lv. more.")