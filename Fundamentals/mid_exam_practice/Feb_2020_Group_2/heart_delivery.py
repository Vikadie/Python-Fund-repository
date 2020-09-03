neighborhood_houses = list(map(int, input().split('@')))

command = input()
house_index = 0
while command != "Love!":
    jump, moves = command.split()
    moves = int(moves)
    house_index += moves
    if house_index >= len(neighborhood_houses):
        house_index = 0
    if neighborhood_houses[house_index] == 0:
        print(f"Place {house_index} already had Valentine's day.")
    else:
        neighborhood_houses[house_index] -= 2
        if neighborhood_houses[house_index] == 0:
            print(f"Place {house_index} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {house_index}.")
if sum(neighborhood_houses) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {sum([1 for house_count in neighborhood_houses if house_count > 0])} places.")
