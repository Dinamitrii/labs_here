import turtle
import math

t = turtle.Turtle(); t.speed(0)


colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

for i in range(360):
    t.pencolor(colors[i % 7])
    t.forward(i * 0.5)
    t.right(59)

turtle.done()

