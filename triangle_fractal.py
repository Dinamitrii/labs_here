import turtle

t = turtle.Turtle(); t.speed(0); turtle.bgcolor('black'); t.color('cyan')


def sierpinski(lenght, depth):
    if depth == 0:
        for _ in range(3): t.forward(lenght); t.left(120)
    else:
        sierpinski(lenght/2, depth-1)
        t.forward(lenght/2)
        sierpinski(lenght/2, depth-1)
        t.backward(lenght/2); t.left(60)
        t.forward(lenght/2); t.right(60)
        sierpinski(lenght/2, depth-1)
        t.left(60); t.backward(lenght/2); t.right(60)


sierpinski(350, 4)

turtle.done()



