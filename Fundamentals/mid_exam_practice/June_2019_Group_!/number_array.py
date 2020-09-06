numbers = list(map(int, input().split()))

commands = input()

while commands != 'End':
    command, tokens = commands.split(' ', 1)
    if command == 'Switch':
        index = int(tokens)
        if 0 <= index < len(numbers):
            numbers[index] *= -1
    if command == 'Change':
        index, value = tuple(map(int, tokens.split()))
        if 0 <= index < len(numbers):
            numbers[index] = value
    if command == 'Sum':
        summ = 0
        if tokens == 'Negative':
            for num in numbers:
               if num < 0:
                   summ += num
        elif tokens == 'Positive':
            for num in numbers:
                if num > 0:
                    summ += num
        else:
            summ = sum(numbers)
        print(summ)

    commands = input()
#[print(num, end = " ") for num in numbers if num >= 0]
print(' '.join([str(num) for num in numbers if num >= 0]))
