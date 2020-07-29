food_daily = float(input())
souvenirs_money = float(input())
hotel_per_day = float(input())

# 210 километра, Тяхната кола изразходва средно по 7 литра на всеки 100 километра, а цената на бензина е 1,85 лв. за един литър.
travel_cost = 4.2 * 7 * 1.85 # both directions
hotel_day_1 = hotel_per_day * 0.9
hotel_day_2 = hotel_per_day * 0.85
hotel_day_3 = hotel_per_day * 0.8
hotel_cost = hotel_day_1 + hotel_day_2 + hotel_day_3

total_cost = hotel_cost + food_daily * 3 + souvenirs_money * 3 + travel_cost

print(f'Money needed: {total_cost:.2f}')