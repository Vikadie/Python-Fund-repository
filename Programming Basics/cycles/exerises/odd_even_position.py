import sys

n = int(input())

biggest_odd = -sys.maxsize
biggest_even = -sys.maxsize
smallest_odd = sys.maxsize
smallest_even = sys.maxsize
sum_even = sum_odd = 0

for i in range(1, n + 1):
    number = float(input())
    if i % 2 == 0:  # even
        sum_even += number
        if number > biggest_even:
            biggest_even = number
        if number < smallest_even:
            smallest_even = number

    if i % 2 != 0:  # odd
        sum_odd += number
        if number > biggest_odd:
            biggest_odd = number
        if number < smallest_odd:
            smallest_odd = number

print(f'OddSum={sum_odd:.2f},')
print(f'OddMin={smallest_odd:.2f},') if smallest_odd != sys.maxsize else print('OddMin=No,')
print(f'OddMax={biggest_odd:.2f},') if biggest_odd != -sys.maxsize else print('OddMax=No,')
print(f'EvenSum={sum_even:.2f},')
print(f'EvenMin={smallest_even:.2f},') if smallest_even != sys.maxsize else print('EvenMin=No,')
print(f'EvenMax={biggest_even:.2f}') if biggest_even != -sys.maxsize else print('EvenMax=No')