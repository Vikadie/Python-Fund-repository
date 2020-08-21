from math import floor

target = float(input())
nr_fantasy = int(input())
nr_horror = int(input())
nr_romance = int(input())

fantasy = 14.9 * nr_fantasy
horror = 9.8 * nr_horror
romance = 4.3 * nr_romance

sum = 0.8 * (fantasy + horror + romance)

if sum >= target:
    sellers_salary = floor(0.1 * (sum - target))
    donation = sum - sellers_salary
    print("%.2f" %donation, "leva donated.")
    print(f"Sellers will receive {sellers_salary} leva.")
else:
    print("%.2f" % (target-sum), "money needed.")

