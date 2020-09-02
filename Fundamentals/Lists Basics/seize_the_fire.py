def check_correct_fire_level(fire_level, num):
    check = (
        (fire_level == 'High' and 81 <= num <= 125) or
        (fire_level == 'Medium' and 51 <= num <= 80) or
        (fire_level == 'Low' and 1 <= num <= 50)
    )
    return check

fire_w_cells = input().split('#')
water = int(input())

cells_for_print = []
effort = 0
for cell in fire_w_cells:
    fire_level, num_str = cell.split(' = ')
    num = int(num_str)
    if check_correct_fire_level(fire_level, num):
        if num <= water:  # in case we have enough water
            cells_for_print.append(num)  # append to cells that are going to be printed
            water -= num  # reducing the water
            effort += num * 0.25  # calculating and adding the effort

total_fire = sum(cells_for_print)
print("Cells:")
for i in cells_for_print:
    print(f" - {i}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")