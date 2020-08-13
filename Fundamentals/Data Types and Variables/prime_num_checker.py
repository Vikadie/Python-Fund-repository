num = int(input())

prime = True
for i in range(2, int(pow(num, 0.5)) + 1):
    if num % i == 0:
        prime = False
        break

print(prime)