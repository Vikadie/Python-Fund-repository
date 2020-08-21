from math import floor

kg_lemons = float(input())
kg_sugar = float(input())
l_water = float(input())

#kg_lemon = 0.98 l juice
#0.98 l juice + kg_sugar = 0.98 l juic + 0,3*kg_sugar
l_juice = kg_lemons * 0.98 + 0.3 * kg_sugar + l_water
# we accept 1 l = 1 kg
# 1 cup juice = 150 ml on price 1.20 lv
cup_number = floor(l_juice / 0.15)

print(f"All cups sold: {cup_number}")
print(f"Money earned: {cup_number * 1.2:.2f}")

