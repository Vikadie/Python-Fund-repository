from math import floor

name = input()

all_games = int(input())
if all_games < 1: quit()

count_v, count_t, count_b, sum_v, sum_t, sum_b = 0, 0, 0, 0, 0, 0

for _ in range(all_games):
    #game = input()
    #points = float(input())

    while True:
        game = input()
        if game ==  "volleyball" or game == "tennis" or game == "badminton":
            # print("Game is", game)
            points = float(input())
            break
        else:
            print("Try again with the name of this game: ")
            continue

    if game == "volleyball":
        points = points * 1.07
        count_v += 1
        sum_v += points
    elif game == "tennis":
        points = points * 1.05
        count_t += 1
        sum_t += points
    elif game == "badminton":
        points = points * 1.02
        count_b += 1
        sum_b += points

total = floor(sum_v + sum_t + sum_b)

if count_v > 0:
    aver_v = sum_v/count_v
else:
    aver_v = 75
if count_t > 0:
    aver_t = sum_t/count_t
else:
    aver_t = 75
if count_b > 0:
    aver_b = sum_b/count_b
else:
    aver_b = 75

if aver_v >= 75 and aver_t >= 75 and aver_b >= 75:
    print(f"Congratulations, {name}! You won the cruise games with {total} points.")
else:
    print(f"Sorry, {name}, you lost. Your points are only {total}.")