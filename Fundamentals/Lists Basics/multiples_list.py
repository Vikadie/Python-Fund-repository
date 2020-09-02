factor = int(input())
count = int(input())

ans = []
for i in range(1, count + 1):
    ans.append(i*factor)

print(ans)