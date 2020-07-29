from math import pi

figure = input()


def side():
    x = float(input())
    return x


if figure == "square":
    print("%.3f" % side() ** 2)
elif figure == "rectangle":
    print("%.3f" % (side() * side()))
elif figure == "circle":
    print("%.3f" % (pi * side() ** 2))
elif figure == "triangle":
    print("%.3f" % (side() * side() / 2))
