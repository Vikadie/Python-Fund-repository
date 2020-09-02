collection_of_items = input().split('|')
budget = float(input())

bought_items_list = [] # we will use this list only for bought items
for item_type in collection_of_items:
    item, price_str = item_type.split('->')
    price = float(price_str)
    check_price = ((item == 'Clothes' and price <= 50) or
                   (item == 'Shoes' and price <= 35) or
                   (item == 'Accessories' and price <= 20.5)
                   )
    if check_price and budget >= price: # check the price is valid and they can allow it based on their budget
        budget -= price
        bought_items_list.append(price)

new_list = [price * 1.4 for price in bought_items_list] # list of same items with +40% increase in price
for new_price in new_list:
    print(f"{new_price:.2f} ", end="")

#print(*new_list)
profit = sum(new_list) - sum(bought_items_list) # calculate the profit
print(f"\nProfit: {profit:.2f}")
if (budget + sum(new_list) >= 150):
    print("Hello, France!")
else:
    print("Time to go.")

