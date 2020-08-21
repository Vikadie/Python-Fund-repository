import turtle

my_turtle = turtle.Turtle()

my_turtle.shape('turtle')
for j in range(3):
    my_turtle.left(120)
    t = 0
    for i in range(7):
        t += 10
        my_turtle.left(120)
        my_turtle.forward(t)
        t += 10
        my_turtle.left(120)
        my_turtle.forward(t)
        t += 10
        my_turtle.left(120)
        my_turtle.forward(t)

        my_turtle.color('red')
print('t =', t)
my_turtle.pensize(10)
for i in range(5):
    my_turtle.left(50)
    my_turtle.forward(t)
    my_turtle.left(120)
    my_turtle.forward(t)
    my_turtle.left(120)
    my_turtle.forward(t)
my_turtle.pensize(5)
# t = 300
for i in range(1, 37):
    if i % 3 == 0 :
        my_turtle.color('yellow')
    elif i % 5 == 0 :
        my_turtle.color('pink')
    elif i % 2 ==0:
        my_turtle.color('green')
    else:
        my_turtle.color('purple')
    # if i > 37:
    #     t = 150
    my_turtle.left(5)
    my_turtle.forward(t)
    my_turtle.left(170)
    my_turtle.forward(t)