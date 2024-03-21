from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]


for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-230, y=y_positions[turtle_index])


# def make_turtle(color, y_position):
#     tim = Turtle(shape="turtle")
#     tim.penup()
#     tim.color(color)
#     tim.goto(x=-230, y=y_position)


# red = make_turtle(colors[0], -100)
# orange = make_turtle(colors[1], -60)
# yellow = make_turtle(colors[2], -20)
# green = make_turtle(colors[3], 20)
# blue = make_turtle(colors[4], 60)
# purple = make_turtle(colors[5], 100)

# user_bet = screen.textinput(
#     title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
# )
# print(user_choice)

screen.exitonclick()
