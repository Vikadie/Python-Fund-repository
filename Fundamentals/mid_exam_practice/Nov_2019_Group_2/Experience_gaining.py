needed_experience_to_unlock = float(input())
count_of_battles = int(input())

sum_experience, battle_count = 0, 0
for battle in range(1, count_of_battles + 1):
    experience_earned = float(input())
    if battle % 3 == 0:
        experience_earned *= 1.15
    elif battle % 5 == 0:
        experience_earned *= 0.9
    sum_experience += experience_earned
    battle_count += 1
    if sum_experience >= needed_experience_to_unlock:
        break

if sum_experience >= needed_experience_to_unlock:
    print(f"Player successfully collected his needed experience for {battle_count} battles.")
else:
    missing_experience = needed_experience_to_unlock - sum_experience
    print(f"Player was not able to collect the needed experience, {missing_experience:.2f} more needed.")
