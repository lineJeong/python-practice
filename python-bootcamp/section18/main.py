import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

# GAP = 5
# while GAP <= 360:
#     tim.color(random_color())
#     tim.circle(100)
#     tim.setheading(GAP)
#     GAP += 5


# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")

# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# colors = [
#     "aquamarine",
#     "IndianRed",
#     "dark sea green",
#     "medium sea green",
#     "DarkOrchid",
#     "green yellow",
#     "lime",
#     "olive drab",
# ]

# for _ in range(200):
#     tim.color(random.choice(colors))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

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

screen = t.Screen()
screen.exitonclick()
