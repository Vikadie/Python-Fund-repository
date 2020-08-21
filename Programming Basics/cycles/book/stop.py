n = int(input())

frame_left = '//'
frame_right = '\\\\'
stop_row = frame_left + '_' * int((4 * n - 1) / 2 - 2.5) + 'STOP!' + '_' * int((4 * n - 1) / 2 - 2.5) + frame_right
top = '.' * (n + 1) + '_' * (2 * n + 1) + '.' * (n + 1)

print(top)
for i in range(n):
    print('.' * (n - i) + frame_left + '_' * (2 *(n + i) - 1) + frame_right + '.' * (n - i))

print(stop_row)

for i in range(n, 0, -1):
    print('.' * (n - i) + frame_right + '_' * (2 * (n + i) - 1) + frame_left + '.' * (n - i))
