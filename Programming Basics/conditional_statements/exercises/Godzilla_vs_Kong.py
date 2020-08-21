film_budget = float(input())
actors_stat = int(input())
dress_price = float(input())

decors = 0.1 * film_budget
dress_budget = actors_stat * dress_price

if actors_stat > 150:
    dress_budget *= 0.9

if (decors + dress_budget) > film_budget:
    print("Not enough money!")
    print(f"Wingard needs {((decors + dress_budget) - film_budget):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {(film_budget - (decors + dress_budget)):.2f} leva left.")
