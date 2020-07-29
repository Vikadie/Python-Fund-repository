floors = int(input())
apartment = int(input())

for i in range(floors, 0, -1):
    if i == floors:
        type = 'L'
    elif i % 2 == 0:
        type = 'O'
    else:
        type = 'A'
    for j in range(apartment):
        print(f'{type}{i}{j}', end = " ")
        if j == apartment - 1:
            print()