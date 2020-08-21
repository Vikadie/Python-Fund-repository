command = input()
sum = 0
while command != 'Stop':
    curr_number = int(command)
    sum += curr_number
    command = input()

print(sum)