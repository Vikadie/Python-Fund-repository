events = input().split('|')
energy, coins = 100, 100
bankrupt = False
for e in events:
    event, num_str = e.split('-')
    num = int(num_str)
    if event == 'rest':
        energy_new = energy + num
        if energy_new > 100:
            print(f"You gained {100 - energy} energy.")
            energy = 100
        else:
            print(f"You gained {energy_new - energy} energy.")
            energy = energy_new
        print(f"Current energy: {energy}.")
    elif event == 'order':
        if energy < 30:
            energy += 50
            print("You had to rest!")
        else:
            energy -= 30
            print(f"You earned {num} coins.")
            coins += num
    else:
        if coins > num:
            coins -= num
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            bankrupt = True
            break

if not bankrupt:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")