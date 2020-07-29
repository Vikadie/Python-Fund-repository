spaceship_width = float(input())
spaceship_length = float(input())
spaceship_height = float(input())
average_height_astronaut = float(input())

# Below is the correct way to calculate it:
# floors = 1
# if spaceship_height >= average_height_astronaut + 0.4:
#     floors = spaceship_height // (average_height_astronaut + 0.4)
#
# spaceship_area = spaceship_length * spaceship_width
#
# rooms_per_floor = spaceship_area // (2 * 2) # room space = 2m length x 2m width
#
# total_rooms = rooms_per_floor * floors # total rooms = total astronauts

# the way it is requested to calculate it (which is wrong):
spaceship_volume = spaceship_width * spaceship_length * spaceship_height
room_volume = (average_height_astronaut + 0.4) * 2 * 2

total_rooms = (spaceship_volume // room_volume)

if total_rooms < 3:
    print('The spacecraft is too small.')
elif total_rooms > 10:
    print('The spacecraft is too big.')
else:
    print(f'The spacecraft holds {int(total_rooms)} astronauts.')