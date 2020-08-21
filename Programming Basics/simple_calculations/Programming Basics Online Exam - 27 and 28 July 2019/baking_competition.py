participants = int(input())

sum, all_sweets, cookies, cakes, waffles = 0, 0, 0, 0, 0

cookies_price = 1.5
cakes_price = 7.8
waffles_price = 2.3

for i in range(participants):
    name = input()

    while True:
        sweets_type = input()  # cookies, cakes, waffles
        if sweets_type == "Stop baking!":
            print(f"{name} baked {cookies} cookies, {cakes} cakes and {waffles} waffles.")
            all_sweets += (cookies + cakes + waffles)
            sum += (cookies * cookies_price + cakes * cakes_price + waffles * waffles_price)
            cookies, cakes, waffles = 0, 0, 0
            break
        pieces = int(input())

        if sweets_type == "cookies":
            cookies += pieces
        elif sweets_type == "cakes":
            cakes += pieces
        elif sweets_type == "waffles":
            waffles += pieces

print(f"All bakery sold: {all_sweets}")
print(f"Total sum for charity: {sum:.2f} lv.")