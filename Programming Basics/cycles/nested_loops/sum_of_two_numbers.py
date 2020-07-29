beginning = int(input())
end = int(input())
magic_num = int(input())

combination = 0
is_printed = False
for i in range(beginning, end+1):
    if is_printed:
        break
    for j in range(beginning, end+1):
        combination += 1
        if (i + j == magic_num):
            print(f'Combination N:{combination} ({i} + {j} = {magic_num})')
            is_printed = True
            break

if not is_printed:
    print(f'{combination} combinations - neither equals {magic_num}')