n = int(input())
count = 0
new_line = 1
for i in range(1, n + 1):
    print(i, end=" ")
    count += 1
    if count == new_line:
        print()
        new_line += 1
        count = 0