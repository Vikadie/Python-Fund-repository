steps_made = int(input())
step_distance = float(input())
distance_to_travel = int(input())

distance_in_step = 0
for step in range(1, steps_made + 1):
    if step % 5 == 0:
        distance_in_step += step_distance * 0.7
    else:
        distance_in_step += step_distance

percentage = distance_in_step / distance_to_travel
print(f"You travelled {percentage:.2f}% of the distance!")
