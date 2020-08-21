projection_type = input()
rows = int(input())
columns = int(input())

price = 0
if projection_type == "Premiere":
    price = 12
elif projection_type == "Normal":
    price = 7.5
elif projection_type == "Discount":
    price = 5

income = rows * columns * price

print(f'{income:.2f} leva')