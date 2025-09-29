import turtle
import colorsys

t = turtle.Turtle()

turtle.bgcolor("black")

t.speed(0)

colors = [colorsys.hsv_to_rgb(_ / 36, 1.0, 1.0) for _ in range(36)]

for i in range(36):
    t.color(colors[i])
    t.circle(100)
    t.left(10)

turtle.done()



