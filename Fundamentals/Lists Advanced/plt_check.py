problematic_list = input().split(', ')

if len(problematic_list) <= 3:
    rows = 1
    cols = len(problematic_list)
else:
    cols = 3
    if len(problematic_list) % 3 == 0:
        rows = len(problematic_list) // 3
    else:
        rows = len(problematic_list) // 3 + 1

print(rows, cols)
