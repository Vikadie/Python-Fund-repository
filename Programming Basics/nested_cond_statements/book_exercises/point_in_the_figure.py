number_h = int(input())
point_x = int(input())
point_y = int(input())

# designing the figure compposed by figure 1 and figure 2
# figure 1:
x11 = y11 = 0
x12 = 3 * number_h
y12 = number_h
# figure 2:
x21 = y21 = number_h
x22 = 2 * number_h
y22 = 4 * number_h



inside_x_1_down = (x11 < point_x < x12)
inside_y_1 = (y11 < point_y < y12)
inside_x_2 = (x21 < point_x < x22)
inside_y_2 = (y21 < point_y < y22)
inside_x_1_up = ((x11 < point_x < x21) and (x22 < point_x < x12))

common_border = (point_y == y21 and x21 < point_x < x22)

if (inside_x_1_up and inside_y_1) or (inside_x_2 and inside_y_2) or common_border:
    print('inside')
elif (((point_y == y11 and inside_x_1_down) or ((point_x == x11 or point_x == x12) and inside_y_1) or
       (point_y == y22 and inside_x_2) or ((point_x == x21 or point_x == x22) and inside_y_2)) or
      (inside_x_1_up and point_y == y21)):
    print('border')
else:
    print('outside')