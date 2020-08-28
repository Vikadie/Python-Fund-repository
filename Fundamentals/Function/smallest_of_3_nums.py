num1 = int(input())
num2 = int(input())
num3 = int(input())


def smallest(x, y, z):
    if x <= y <= z or x <= z <= y:
        return x
    elif y <= x <= z or y <= z <= x:
        return y
    else:
        return z


print(smallest(num1, num2, num3))