import turtle as t
import random

color_list = [
    (207, 160, 82),
    (54, 88, 130),
    (145, 91, 40),
    (140, 26, 49),
    (221, 207, 105),
    (132, 177, 203),
    (158, 46, 83),
    (45, 55, 104),
    (169, 160, 39),
    (129, 189, 143),
    (83, 20, 44),
    (37, 43, 67),
    (186, 94, 107),
    (187, 140, 170),
    (85, 120, 180),
    (59, 39, 31),
    (88, 157, 92),
    (78, 153, 165),
    (194, 79, 73),
    (45, 74, 78),
    (80, 74, 44),
    (161, 201, 218),
    (57, 125, 121),
    (219, 175, 187),
    (169, 206, 172),
    (219, 182, 169),
]

t.colormode(255)

tim = t.Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.penup()
tim.setposition(-225, -225)


def set_y_axis():
    y_pos = tim.ycor()
    for _ in range(10):
        set_x_axis()
        y_pos += 50
        tim.sety(y_pos)


def set_x_axis():
    x_pos = tim.xcor()
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        x_pos += 50
        tim.setx(x_pos)
    x_pos = -225
    tim.setx(x_pos)


set_y_axis()

screen = t.Screen()
screen.exitonclick()
