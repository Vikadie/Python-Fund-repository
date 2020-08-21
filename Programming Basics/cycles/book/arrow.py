n = int(input())

dots_up = '.' * (n//2)
mid_up = '#' + '.' * (n - 2) + '#'
start = dots_up + '#' * n + dots_up
print(start)
for i in range(n - 2):
    print(dots_up + mid_up + dots_up)
mid = '#' * (n//2) + mid_up + '#' * (n // 2)
print(mid)
top = '.' * (n - 1) + '#' + '.' * (n - 1)
for i in range(n - 2, 0, -1):
    narrow_part = '.' * (n - 1 - i) + '#' + '.' * (2 * i - 1) + '#' + '.' * (n - 1 - i)
    print(narrow_part)

print(top)