entry = list(map(int, input().split(', ')))
beggars = int(input())

ans = []
for b in range(beggars):
    sum = 0
    for i, num in enumerate(entry):
        if i - b == 0 or (i - b) % beggars == 0:
            sum += num
    ans.append(sum)

print(ans)
