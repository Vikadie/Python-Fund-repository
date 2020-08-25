num1 = int(input())
num2 = int(input())
num3 = int(input())


def add_and_subtract(x, y, z):

    def sum_numbers(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    return subtract(sum_numbers(x, y), z)


print(add_and_subtract(num1, num2, num3))