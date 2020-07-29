N = int(input())

for number in range(1111, 10000):
    answer = number
    while number > 0:
        last = number % 10
        if last != 0 and N % last == 0:
            number = number // 10
        else:
            break
    if number == 0:
        print(answer, end=" ")