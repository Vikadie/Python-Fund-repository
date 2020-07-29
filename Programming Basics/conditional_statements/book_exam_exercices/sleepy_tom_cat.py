vacation_days = int(input())

play_norm = 30000  # minutes / year

working_day = 365 - vacation_days

play_time = working_day * 63 + vacation_days * 127

H = abs(play_time - play_norm) // 60
M = abs(play_time - play_norm) % 60

if play_time < play_norm:
    print('Tom sleeps well')
    print(f'{H} hours and {M} minutes less for play')
else:
    print('Tom will run away')
    print(f'{H} hours and {M} minutes more for play')
