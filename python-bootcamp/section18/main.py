from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("SeaGreen")

colors = [
    "aquamarine",
    "IndianRed",
    "dark sea green",
    "medium sea green",
    "DarkOrchid",
    "green yellow",
    "lime",
    "olive drab",
]

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))

# for n in range(3, 11):
#     angle = 360 / n
#     for _ in range(n):
#         tim.forward(100)
#         tim.right(angle)

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)


# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
