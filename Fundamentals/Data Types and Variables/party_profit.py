companions = int(input())
days = int(input())
coins = 0
for d in range(1, days + 1):
    if d % 10 == 0:
        companions -= 2
    if d % 15 == 0:
        companions += 5

    coins += 50
    coins -= 2 * companions

    if (d % 3 == 0):
        coins -= 3 * companions
        if d % 5 == 0:
            coins -= 2 * companions
    if (d % 5 == 0):
        coins += 20 * companions



print(f"{companions} companions received {int(coins/companions)} coins each.")