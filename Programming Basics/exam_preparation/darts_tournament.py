starting_points = int(input())
moves_count = 0
bullseye_hit = False
while starting_points > 0:
    section = input()
    moves_count += 1
    if section == 'bullseye':
        bullseye_hit = True
        break
    section_points = int(input())

    if section == 'number section':
        section_points = section_points
    elif section == 'double ring':
        section_points *= 2
    elif section == 'triple ring':
        section_points *= 3

    starting_points -= section_points

if bullseye_hit:
    print(f'Congratulations! You won the game with a bullseye in {moves_count} moves!')
else:
    if starting_points == 0:
        print(f'Congratulations! You won the game in {moves_count} moves!')
    elif starting_points < 0:
        print(f'Sorry, you lost. Score difference: {abs(starting_points)}.')
