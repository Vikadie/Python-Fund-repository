archery_fields = list(map(int, input().split('|')))

commands_by_judges = input()

collected_points = 0

while commands_by_judges != 'Game over':
    if commands_by_judges == 'Reverse':
        archery_fields = archery_fields[::-1]
    else:
        shoot, left_or_right = commands_by_judges.split()
        l_or_r, start_index, length = left_or_right.split('@')
        start_index = int(start_index)
        length = int(length)
        if 0 <= start_index < len(archery_fields):
            if l_or_r == 'Left':
                index = start_index - length
                while index < -len(archery_fields):
                    index += len(archery_fields)
            else:
                index = start_index + length
                while index >= len(archery_fields):
                    index -= len(archery_fields)
            archery_fields[index] -= 5
            collected_points += 5
            if archery_fields[index] < 0:
                collected_points += archery_fields[index]
                archery_fields[index] = 0

    commands_by_judges = input()

archery_fields_str = [str(i) for i in archery_fields]
print(' - '.join(archery_fields_str))
print(f"Iskren finished the archery tournament with {collected_points} points!")