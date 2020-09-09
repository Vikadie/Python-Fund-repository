shops_list = input().split()

for n in range(int(input())):
    commands = input().split()
    if commands[0] == 'Include':
        shops_list.append(commands[1])
    elif commands[0] == 'Visit':
        number_of_shops = int(commands[2])
        if number_of_shops <= len(shops_list):
            if commands[1] == 'first':
                shops_list = shops_list[number_of_shops:]
            else:
                shops_list = shops_list[: -number_of_shops]
    elif commands[0] == 'Prefer':
        shop_index_1 , shop_index_2 = int(commands[1]), int(commands[2])
        if 0 <= shop_index_1 < len(shops_list) and 0 <= shop_index_2 < len(shops_list):
            shops_list[shop_index_1], shops_list[shop_index_2] = shops_list[shop_index_2], shops_list[shop_index_1]
    elif commands[0] == 'Place':
        shop, shop_index = commands[1], int(commands[2])
        if 0 <= shop_index < len(shops_list):
            shops_list.insert(shop_index + 1, shop)


print("Shops left:")
print(' '.join(shops_list))
