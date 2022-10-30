from math import sin, cos
from turtle import Screen, Turtle


def xt(t):
    return 16 * sin(t) ** 3


def yt(t):
    return 13 * \
        cos(1 * t) - 5 * \
        cos(2 * t) - 2 * \
        cos(3 * t) - \
        cos(4 * t)


screen = Screen()
screen.setup(1040, 1080)
screen.bgcolor('black')
screen.colormode(255)
screen.register_shape("picture.gif")


turtle = Turtle()
turtle.hideturtle()
turtle.speed('fastest')

for i in range(300):
    turtle.goto((xt(i) * 20, yt(i) * 20))
    turtle.pencolor((255 - i) % 255, i % 255, (255 + i) // 2 % 255)
    turtle.home()

turtle.shape("picture.gif")
turtle.stamp()

screen.mainloop()
