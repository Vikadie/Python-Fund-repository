n = int(input())

sum_even = sum_odd = 0
for position in range(n):
    number = int(input())
    if position % 2 == 0:
        sum_even += number
    else:
        sum_odd += number

if sum_even == sum_odd:
    print('Yes')
    print('Sum =', sum_odd)
else:
    print('No')
    print(f'Diff = {abs(sum_odd - sum_even)}')
