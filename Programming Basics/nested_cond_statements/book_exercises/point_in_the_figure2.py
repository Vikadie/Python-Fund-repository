number_h = int(input())
point_x = int(input())
point_y = int(input())

# designing the figure composed by figure 1 and figure 2
# figure 1:
x11 = y11 = 0
x12 = 3 * number_h
y12 = number_h
# figure 2:
x21 = y21 = number_h
x22 = 2 * number_h
y22 = 4 * number_h


inside_fig_1 = (x11 < point_x < x12 and y11 < point_y < y12)
inside_fig_2 = (x21 < point_x < x22 and y21 <= point_y < y22)  # including the lower side

border_fig_1 = ((point_x == x11 or point_x == x12) and y11 <= point_y <= y12) or (point_y == y12 and (x11 <= point_x <= x21 or x22 <= point_x <= x12)) or (point_y == y11 and x11 <= point_x <= x12)
border_fig_2 = ((point_x == x21 or point_x == x22) and y21 <= point_y <= y22) or (point_y == y22 and (x21 <= point_x <= x22))

if inside_fig_1 or inside_fig_2:
    print('inside')
elif border_fig_1 or border_fig_2:
    print('border')
else:
    print('outside')