name = input()

max_score = 0
best_player_name =""

while name != 'END':
    goals = int(input())

    if goals > max_score:
        max_score = goals
        best_player_name = name

    if goals >= 10:
        break;

    name = input()

print(f"{best_player_name} is the best player!")
if max_score >= 3:
    print(f"He has scored {max_score} goals and made a hat-trick!!!")
else:
    print(f"He has scored {max_score} goals.")