init_point = int(input())

if init_point <= 100:
    bonus = 5
elif init_point < 1000:
    bonus = 0.2 * init_point
else:
    bonus = 0.1 * init_point

if init_point % 2 == 0:
    bonus += 1
elif init_point % 10 == 5:
    bonus += 2

points = init_point + bonus

print(f"{bonus}\n{points}")
