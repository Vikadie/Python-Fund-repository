bakers_num = int(input())
ttl_sum_for_charity = 0
all_bakery = 0
cookies_count, cakes_count, waffles_count = 0, 0, 0
while bakers_num > 0:
    baker_name = input()
    bakers_num -= 1
    while True:
        cookie_type = input()
        if cookie_type == 'Stop baking!':
            print(f'{baker_name} baked {cookies_count} cookies, {cakes_count} cakes and {waffles_count} waffles.')
            cookies_count, cakes_count, waffles_count = 0, 0, 0
            break
        cookie_type_count = int(input())

        if cookie_type == 'cookies':
            sum = 1.5 * cookie_type_count
            cookies_count += cookie_type_count
        elif cookie_type == 'cakes':
            sum = 7.8 * cookie_type_count
            cakes_count += cookie_type_count
        elif cookie_type == 'waffles':
            sum = 2.3 * cookie_type_count
            waffles_count += cookie_type_count

        ttl_sum_for_charity += sum
        all_bakery += cookie_type_count

print(f'All bakery sold: {all_bakery}')
print(f'Total sum for charity: {ttl_sum_for_charity:.2f} lv.')