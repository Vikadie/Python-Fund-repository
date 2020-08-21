money_needed = float(input())
saved_money = float(input())
days_count = 5
total_days = 0
cant_save = False
while True:
    if days_count == 0:
        cant_save = True
        break
    elif saved_money >= money_needed:
        break
    spend_or_save = input().lower()
    amount = float(input())
    total_days += 1
    if spend_or_save == 'spend':
        days_count -= 1
        saved_money -= amount
        if saved_money < 0:
            saved_money = 0
    elif spend_or_save == 'save':
        days_count = 5
        saved_money += amount

if cant_save:
    print("You can't save the money.")
    print(total_days)
else:
    print(f'You saved the money for {total_days} days.')