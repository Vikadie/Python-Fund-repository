going_home = False
step_counter = 0
while True:
    steps = input()

    if steps == 'Going home':
        going_home = True
        continue

    step_counter += int(steps)
    if step_counter >= 10000:
        print('Goal reached! Good job!')
        break
    elif going_home:
        print(f'{(10000 - step_counter)} more steps to reach goal.')
        break
