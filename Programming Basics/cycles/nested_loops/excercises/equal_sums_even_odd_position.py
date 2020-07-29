first_num = int(input())
last_num = int(input())

for number in range(first_num, last_num + 1):
#    str_num = str(number)
    even_sum = 0
    odd_sum = 0
#    for index, digit in enumerate(str_num):
#    for index in range(len(str_num)):
#        if index % 2 == 0:
#            even_sum += int(digit)
#            even_sum += int(str_num[index])
#        else:
#            odd_sum += int(digit)
#            odd_sum += int(str_num[index])
#    if even_sum == odd_sum:
#        print(number, end=" ")
    counter = 1
    answer = number
    while number > 0:
        last = number % 10
        if counter % 2 == 0:
            even_sum += last
        else:
            odd_sum += last
        number = number // 10
        counter += 1
    if even_sum == odd_sum:
        print(answer, end=" ")