from turtle import *

def draw_branch(branch_length, angle, trunc_weight):
    if branch_length > 5:
        if trunc_weight < 0:
            trunc_weight = 0
        pensize(trunc_weight)
        forward(branch_length)
        right(angle)
        draw_branch(branch_length - 15, angle, trunc_weight - 4)
        left(2 * angle)
        draw_branch(branch_length - 15, angle, trunc_weight - 4)
        right(angle)
        backward(branch_length)

def draw_tree(trunk_length, angle, trunc_weight):
    speed("fastest")
    left(90)
    up()
    backward(trunk_length)
    down()
    draw_branch(trunk_length, angle, trunc_weight)
    done()

draw_tree(100, 20, 24)
