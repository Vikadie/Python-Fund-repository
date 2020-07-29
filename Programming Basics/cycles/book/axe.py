n = int(input())

for i in range(n):
    print('-' * 3 * n + '*' + '-' * i + '*' + '-' * (2 * n - (2 + i)))

for i in range(n // 2):
    print('*' * 3 * n + ('*' + '-' * (n - 1)) * 2 )

for i in range(n // 2 - 1):
    print('-' * (3 * n - i) + '*' + '-' * (n -1 + i * 2) + '*' + '-' * (n - 1 - i))

print('-' * (3 * n - n // 2 + 1) + '*' * (2 * n - 1 - n % 2) + '-' * (n - n // 2))