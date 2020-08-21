width_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())

volume_free_space = width_free_space * length_free_space * height_free_space
#free_space = True

while volume_free_space >= 0:
    number_of_computers = input()
    if number_of_computers == 'Done':
        break
    else:
        volume_free_space -= int(number_of_computers)

if volume_free_space >= 0:
    print(f'{volume_free_space} Cubic meters left.')
else:
    print(f'No more free space! You need {abs(volume_free_space)} Cubic meters more.')