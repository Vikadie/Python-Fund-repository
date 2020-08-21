result_match_1 = input()
result_match_2 = input()
result_match_3 = input()

won = lost = drawn = 0

if result_match_1[0] > result_match_1[2]:
    won += 1
elif result_match_1[0] < result_match_1[2]:
    lost += 1
else:
    drawn += 1

if result_match_2[0] > result_match_2[2]:
    won += 1
elif result_match_2[0] < result_match_2[2]:
    lost += 1
else:
    drawn += 1

if result_match_3[0] > result_match_3[2]:
    won += 1
elif result_match_3[0] < result_match_3[2]:
    lost += 1
else:
    drawn += 1

print(f'Team won {won} games.')
print(f'Team lost {lost} games.')
print(f'Drawn games: {drawn}')