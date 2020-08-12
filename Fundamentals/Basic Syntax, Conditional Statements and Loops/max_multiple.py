divisor = int(input())
bound = int(input())

for num in range(bound, divisor - 1, -1):
    if num > 0 and num % divisor == 0:
        print(num)
        break
