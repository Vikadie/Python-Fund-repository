from math import floor

budget = float(input())
price_kg_flour = float(input())
pack_egg_price = 0.75 * price_kg_flour
l_milk = 1.25 * price_kg_flour

cozunac_price = pack_egg_price + price_kg_flour + 0.25* l_milk
total_cozunacs = floor(budget / cozunac_price)
money_left = budget - total_cozunacs * cozunac_price
colored_eggs , curr_cozunacs = total_cozunacs * 3, 0
for cozunac_pcs in range(total_cozunacs):
    curr_cozunacs += 1
    if curr_cozunacs % 3 == 0:
        colored_eggs -= curr_cozunacs - 2

print(f"You made {total_cozunacs} cozonacs! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")

