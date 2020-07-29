excursion = float(input())
num_puzzles = int(input())
num_speaking_dolls = int(input())
num_teddy_bear = int(input())
num_minion = int(input())
num_truck = int(input())

puzzle = 2.6
speaking_doll = 3
teddy_bear = 4.1
minion = 8.2
truck = 2

number = num_minion + num_puzzles + num_speaking_dolls + num_teddy_bear + num_truck
if number >= 50:
    discount = 0.25
else:
    discount = 0

turnover = (puzzle * num_puzzles + speaking_doll * num_speaking_dolls + teddy_bear * num_teddy_bear + num_minion * minion + truck * num_truck) * (1 - discount)
profit = turnover * 0.9

if profit >= excursion:
    print(f"Yes! {(profit - excursion):.2f} lv left.")
else:
    print(f"Not enough money! {(excursion - profit):.2f} lv needed.")