inp = input()

dict_product_price = dict()
dict_product_quantity = dict()
while inp != 'buy':
    product, price, quantity = inp.split()
    dict_product_price[product] = float(price)
    dict_product_quantity[product] = dict_product_quantity.get(product, 0) + int(quantity)

    inp = input()

for product in dict_product_quantity.keys():
    print(f'{product} -> {(dict_product_quantity[product] * dict_product_price[product]):.2f}')