loss = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expense = 0
for l in range (1, loss+1):
    if (l % 2 == 0):
        expense += helmet_price
    if (l % 3 == 0):
        expense +=sword_price
        if (l % 2 == 0):
            expense += shield_price
    if (l % 12 == 0):
        expense += armor_price

print(f"Gladiator expenses: {expense:.2f} aureus")