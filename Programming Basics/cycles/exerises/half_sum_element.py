import sys

number_count = int(input())

biggest_num = - sys.maxsize
sum = 0

for i in range(number_count):
    number = int(input())
    if number > biggest_num:
        biggest_num = number
    sum += number

if (sum - biggest_num) == biggest_num:
    print("Yes")
    print('Sum =', biggest_num)
else:
    print('No')
    print('Diff =', abs(biggest_num - (sum - biggest_num)))