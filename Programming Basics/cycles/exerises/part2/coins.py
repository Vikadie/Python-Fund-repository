amount = int(100 * float(input()))
count_coins = 0

for coin_type in [200, 100, 50, 20, 10, 5, 2, 1]:
    if amount // coin_type >= 0:
        count_coins += amount // coin_type
        amount = amount % coin_type

print(count_coins)