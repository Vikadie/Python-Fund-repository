rows = int(input())

matrix = []
for _ in range(rows):
    matrix.append(list(map(int, input().split())))

destroyed_ships = 0
attacks = input().split()
for attack in attacks:
    i, j = map(int, attack.split('-'))
    if matrix[i][j] > 0:
        matrix[i][j] -= 1
        if matrix[i][j] == 0:
            destroyed_ships += 1

print(destroyed_ships)