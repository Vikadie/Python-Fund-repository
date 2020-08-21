divisor = int(input())
bound = int(input())

n = bound
while True:
    if n % divisor == 0 and n <= bound and n > 0:
        print(n)
        break
    else:
        n -= 1