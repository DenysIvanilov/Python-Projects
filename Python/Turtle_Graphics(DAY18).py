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

turtle.clear()
# Drawing Different Shapes
for i in range(3, 11):
    angle = 360 / i
    for _ in range(i):
        turtle.rt(angle)
        turtle.fd(100)
screen = Screen()
screen.exitonclick()
