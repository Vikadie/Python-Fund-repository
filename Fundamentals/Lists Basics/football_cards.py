entry = input().split()
a_list, b_list = [], []

for card in entry:
    team, num = card.split('-')
    if team == 'A':
        if num not in a_list:
            a_list.append(num)
    else:
        if num not in b_list:
            b_list.append(num)

print(f"Team A - {11 - len(a_list)}; Team B - {11 - len(b_list)}")
if len(a_list) > 4 or len(b_list) > 4:
    print("Game was terminated")
