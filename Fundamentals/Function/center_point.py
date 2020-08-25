x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())


def check_dist(x, y):
    return (x * x + y * y)


# def return_lowest(x, y):
#     if x * x < y * y:
#         return (f"({x}, {y})")
#     else:
#         return (f"({y}, {x})")


if check_dist(x1, y1) <= check_dist(x2, y2):
    print(f"({int(x1)}, {int(y1)})")
else:
    print(f"({int(x2)}, {int(y2)})")
