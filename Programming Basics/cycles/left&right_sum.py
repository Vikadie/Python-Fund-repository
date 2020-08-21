n = int(input())

sum_left, sum_right = 0, 0

for left in range(n):
    num_left = int(input())
    sum_left += num_left

for right in range(n):
    num_right = int(input())
    sum_right += num_right

if sum_left == sum_right:
    print('Yes, sum =', sum_left)
else:
    print('No, diff =', abs(sum_left - sum_right))