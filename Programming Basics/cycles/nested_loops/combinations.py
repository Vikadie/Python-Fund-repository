n = int(input())
combinations = 0
for i in range(100):
    for j in range(100):
        for m in range(100):
            if (i + j + m) == n:
                combinations += 1
print(combinations)