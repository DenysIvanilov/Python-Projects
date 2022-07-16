import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")

# Drawing a Square
for _ in range(4):
    timmy.fd(100)
    timmy.lt(90)

timmy.clear()
# Drawing a Dashed Line
for _ in range(15):
    timmy.fd(5)
    timmy.penup()
    timmy.fd(5)
    timmy.pendown()

timmy.clear()
# Drawing Different Shapes( from 3 sides to 10 )
for i in range(3, 11):
    angle = 360 / i
    timmy.color(random_color())
    for _ in range(i):
        timmy.rt(angle)
        timmy.fd(100)

timmy.clear()
# Random Walk
directions = [0, 90, 180, 270]
timmy.pensize(10)
timmy.speed(0)
for _ in range(200):
    timmy.color(random_color())
    timmy.fd(15)
    timmy.setheading(random.choice(directions))

timmy.clear()
timmy.pensize(1)


# Spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
