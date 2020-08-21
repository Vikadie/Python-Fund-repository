width = int(input())
length = int(input())
height = int(input())

total_volume = width * length * height
while True:
    boxes = input()
    if boxes == 'Done':
        print(f'{total_volume} Cubic meters left.')
        break
    if total_volume - int(boxes) > 0:
        total_volume -= int(boxes)
    else:
        print(f'No more free space! You need {int(boxes) - total_volume} Cubic meters more.')
        break
