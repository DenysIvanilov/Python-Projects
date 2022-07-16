import turtle
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")

# Drawing a Square
for _ in range(4):
    turtle.fd(100)
    turtle.lt(90)

turtle.clear()
# Drawing a Dashed Line
for _ in range(15):
    turtle.fd(10)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()


screen = Screen()
screen.exitonclick()
