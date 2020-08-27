num1 = int(input())
num2 = int(input())


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


print(f"{(factorial(num1)/factorial(num2)):.2f}")