N = int(input())
M = int(input())
S = int(input())

for i in range(M, N - 1, -1):
    if i%2 == 0 and i%3 == 0:
        if i == S:
            break
        print(i, end=" ")