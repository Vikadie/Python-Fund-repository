num_str = input()

ans = ""
for i in range(len(str(num_str))):
    max, position = 0, -1
    for count, digit in enumerate(num_str):
        if int(digit) > max:
            max = int(digit)
            position = count
    ans += str(max)
    num_str = num_str[: position] + num_str[position + 1 :]
print(int(ans))