from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("SeaGreen")

# for n in range(3, 11):
#     angle = 360 / n
#     for _ in range(n):
#         tim.forward(100)
#         tim.right(angle)

colors = [
    "aquamarine",
    "medium aquamarine",
    "dark sea green",
    "medium sea green",
    "sea green",
    "green yellow",
    "lime",
    "olive drab",
]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
