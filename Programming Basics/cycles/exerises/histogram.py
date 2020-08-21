n = int(input())

count_199 = count_200_399 = count_400_599 = count_600_799 = count_800_1000 = 0

for i in range(n):
    number = int(input())
    if number < 200:
        count_199 += 1
    elif 200 <= number < 400:
        count_200_399 += 1
    elif 400 <= number < 600:
        count_400_599 += 1
    elif 600 <= number < 800:
        count_600_799 += 1
    else:
        count_800_1000 += 1

print(f'{(100 * count_199 / n):.2f}%')
print(f'{(100 * count_200_399 / n):.2f}%')
print(f'{(100 * count_400_599 / n):.2f}%')
print(f'{(100 * count_600_799 / n):.2f}%')
print(f'{(100 * count_800_1000 / n):.2f}%')