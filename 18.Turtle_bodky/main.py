import turtle
from turtle import Turtle, Screen
from random import choice

color_list = [
    (34, 108, 167),
    (245, 77, 36),
    (112, 163, 211),
    (153, 57, 85),
    (219, 156, 94),
    (201, 60, 27),
    (24, 133, 55),
    (246, 204, 84),
    (190, 151, 47),
    (225, 119, 152),
    (46, 53, 121),
    (221, 68, 97),
    (113, 199, 156),
    (147, 37, 30),
    (253, 202, 0),
    (91, 113, 192),
    (74, 40, 32),
    (248, 153, 143),
    (111, 41, 49),
    (155, 212, 203),
    (53, 174, 163),
    (38, 31, 67),
    (154, 210, 219),
    (43, 33, 45),
    (35, 55, 46),
    (99, 93, 2),
]
john = Turtle()
turtle.colormode(255)
john.shape("classic")
john.hideturtle()
john.speed(0)


def get_to_start(y_value):
    john.up()
    john.setpos(200, y_value)
    john.setheading(180)


def gulicky():
    for i in range(10):
        john.down()
        john.dot(20, choice(color_list))
        john.up()
        john.forward(50)


for y in range(-200, 300, 50):
    get_to_start(y)
    gulicky()
screen = Screen()
screen.exitonclick()
