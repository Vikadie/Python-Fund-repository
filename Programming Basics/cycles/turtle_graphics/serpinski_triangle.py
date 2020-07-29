from turtle import *


def draw_triangle(points, color):
    fillcolor(color)
    up()
    goto(points[0][0], points[0][1])
    down()
    begin_fill()
    goto(points[1][0], points[1][1])
    goto(points[2][0], points[2][1])
    goto(points[0][0], points[0][1])
    end_fill()


def get_mid(p1, p2):
    return ((p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(points, degree):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    draw_triangle(points, colormap[degree])
    if degree > 0:
        sierpinski([points[0], get_mid(points[0], points[1]), get_mid(points[0], points[2])], degree-1)
        sierpinski([points[1], get_mid(points[0], points[1]), get_mid(points[1], points[2])], degree-1)
        sierpinski([points[2], get_mid(points[2], points[1]), get_mid(points[0], points[2])], degree-1)

win = Screen()

my_points = [[-200,-100],[0,200],[200,-100]]
sierpinski(my_points,2)
win.exitonclick()
