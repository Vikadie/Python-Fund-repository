budget = float(input())
price_kg_flour = float(input())

price_pack_eggs = 0.75 * price_kg_flour
price_l_milk = 1.25 * price_kg_flour

cozunac_price = price_pack_eggs + price_kg_flour + 1/4 * price_l_milk
eggs, sum, count = 0, 0, 0

while budget - sum > cozunac_price:
    sum += cozunac_price
    count += 1
    eggs += 3
    if count % 3 == 0:
        eggs -= count - 2

print(f"You made {int(sum/cozunac_price)} cozonacs! Now you have {eggs} eggs and {(budget - sum):.2f}BGN left.")