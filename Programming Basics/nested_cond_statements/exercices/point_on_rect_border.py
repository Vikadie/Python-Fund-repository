x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
given_x = float(input())
given_y = float(input())

if ((given_x == x1 or given_x == x2) and (y1 <= given_y <= y2)) or ((given_y == y1 or given_y == y2) and (x1 <= given_x <= x2)):
    print('Border')
else:
    print('Inside / Outside')
