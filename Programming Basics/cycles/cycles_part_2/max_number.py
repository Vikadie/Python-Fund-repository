from sys import maxsize

n = int(input())
count = 0
biggest_number = - maxsize
while count < n:
    curr_number = int(input())
    if curr_number > biggest_number:
        biggest_number = curr_number
    count += 1

print(biggest_number)