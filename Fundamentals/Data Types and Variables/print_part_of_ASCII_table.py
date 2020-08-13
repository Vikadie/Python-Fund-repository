start = int(input())
end = int(input())

for i in range(end - start + 1):
    print(chr(start + i), end=" ")