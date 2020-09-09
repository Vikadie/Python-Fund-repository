Dineyland_journey_cost = float(input())
months_number = int(input())
saved_amount = 0
for mo in range(1, months_number + 1):
    if mo % 4 == 0:
        saved_amount *= 1.25 # bonus 25% from the boss of the money collected so far
    if mo > 1 and mo % 2 != 0:
        saved_amount *= (1 - 0.16)  # spending 16% for clothes and shoes
    saved_amount += 0.25 * Dineyland_journey_cost


if saved_amount >= Dineyland_journey_cost:
    money = saved_amount - Dineyland_journey_cost
    print(f"Bravo! You can go to Disneyland and you will have {money:.2f}lv. for souvenirs.")
else:
    money = Dineyland_journey_cost - saved_amount
    print(f"Sorry. You need {money:.2f}lv. more.")

