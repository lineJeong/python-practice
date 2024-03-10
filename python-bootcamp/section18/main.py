from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("SeaGreen")

for _ in range(20):
    tim.forward(5)
    tim.penup()
    tim.forward(5)
    tim.pendown()

screen = Screen()
screen.exitonclick()
