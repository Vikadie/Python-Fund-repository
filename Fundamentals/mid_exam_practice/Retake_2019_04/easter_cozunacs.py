budget = float(input())
price_for_kg_flour = float(input())

price_pack_egg = 0.75 * price_for_kg_flour
price_l_milk = 1.25 * price_for_kg_flour
cozunac = price_pack_egg + price_for_kg_flour + 0.25 * price_l_milk

cozunac_count = 0
colored_eggs = 0
while True:
    if budget > cozunac:
        budget -= cozunac
        cozunac_count += 1
        colored_eggs += 3
        if cozunac_count % 3 == 0:
            colored_eggs -= cozunac_count - 2
    else:
        break

print(f"You made {cozunac_count} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
