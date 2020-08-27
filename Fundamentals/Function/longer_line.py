points = []
for _ in range(8):
    points.append(float(input()))

x11, y11, x21, y21, x12, y12, x22, y22 = points


def line_length(x1, y1, x2, y2):
    x = x1 - x2
    y = y1 - y2
    length = pow(x*x + y*y, 1/2)

    return length


def smaller_pair(x1, y1, x2, y2):

    if (abs(x1) + abs(y1)) <= (abs(x2)+ abs(y2)):
        return f"({int(x1)}, {int(y1)})({int(x2)}, {int(y2)})"
    else:
        return f"({int(x2)}, {int(y2)})({int(x1)}, {int(y1)})"


line1 = line_length(x11, y11, x21, y21)
line2 = line_length(x12, y12, x22, y22)

if line1 >= line2:
    print(smaller_pair(x11, y11, x21, y21))
else:
    print(smaller_pair(x12, y12, x22, y22))