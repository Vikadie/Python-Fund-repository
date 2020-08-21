from math import floor

player = input()
games_played = int(input())

total_points_v, total_points_t, total_points_b  = 0, 0, 0
games_played_v, games_played_t, games_played_b = 0, 0, 0
for game in range(games_played):
    game_name = input()
    points = int(input())
    if game_name == 'volleyball':
        points *= 1.07
        total_points_v += points
        games_played_v += 1
    elif game_name == 'tennis':
        points *= 1.05
        total_points_t += points
        games_played_t += 1
    elif game_name == 'badminton':
        points *= 1.02
        total_points_b += points
        games_played_b += 1

aver_points_v, aver_points_t, aver_points_b = 0, 0, 0
won = True
if total_points_v > 0:
    aver_points_v = (total_points_v/games_played_v)
    if aver_points_v < 75:
        won = False
if total_points_t > 0:
    aver_points_t = (total_points_t/games_played_t)
    if aver_points_t < 75:
        won = False
if total_points_b > 0:
    aver_points_b = (total_points_b/games_played_b)
    if aver_points_b < 75:
        won = False

total_points = total_points_b + total_points_t + total_points_v

if won:
    print(f'Congratulations, {player}! You won the cruise games with {floor(total_points)} points.')
else:
    print(f'Sorry, {player}, you lost. Your points are only {floor(total_points)}.')