days = int(input()) #vacation days

limit = 0
products_bought = 0

for d in range(days):
    limit += 60.00 # initialize the daily allowance
    products_bought = 0
    while limit > 0:
        a = input()
        if a == "Day over":
            print(f"Money left from today: {limit:.2f}. You've bought {products_bought} products.")
            break
        else:
            a = float(a)
            if (limit - a) > 0:
                limit = limit - a
                products_bought += 1
                continue
            elif (limit - a) == 0:
                limit = 0
                products_bought += 1
                print(f"Daily limit exceeded! You've bought {products_bought} products.")
                break

