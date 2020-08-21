n = int(input())

count_div_2 = count_div_3 = count_div_4 = 0
for i in range(n):
    number = int(input())
    if number % 2 == 0:
        count_div_2 += 1
    if number % 3 == 0:
        count_div_3 += 1
    if number % 4 == 0:
        count_div_4 += 1

print(f'{(100 * count_div_2 / n):.2f}%')
print(f'{(100 * count_div_3 / n):.2f}%')
print(f'{(100 * count_div_4 / n):.2f}%')