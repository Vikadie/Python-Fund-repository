numbers_list = list(map(int, input().split(", ")))

# if max(numbers_list) % 10 == 0:
#     list_of_lists_size = max(numbers_list) // 10 - 1
# else:
#     list_of_lists_size = max(numbers_list) // 10
#
# list_of_lists = [[] * i for i in range(list_of_lists_size + 1)]
#
# for num in numbers_list:
#     if num % 10 == 0:
#         index = (num - 1) // 10
#     else:
#         index = num // 10
#     list_of_lists[index].append(num)
#
# for index in range(len(list_of_lists)):
#     print(f"Group of {index + 1}0's: {list_of_lists[index]}")
from math import ceil

for i in range(1, ceil(max(numbers_list)/10) +1):

    upper = i * 10
    lower = upper - 10

    current_range = [num for num in numbers_list if lower < num <= upper]

    print(f"Group of {upper}0's: {current_range}")
