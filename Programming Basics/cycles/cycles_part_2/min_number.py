n = int(input())

count = 0
while count < n:
    curr_num = int(input())
    if count == 0:
        smallest_num = curr_num
    elif curr_num < smallest_num:
        smallest_num = curr_num
    count += 1

print(smallest_num)
