import turtle
from turtle import Turtle, Screen
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

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
    timmy.fd(10)
    timmy.penup()
    timmy.fd(10)
    timmy.pendown()

timmy.clear()
# Drawing Different Shapes( from 3 sides to 10 )
for i in range(3, 11):
    angle = 360 / i
    timmy.color(colours[random.randint(0, len(colours) - 1)])
    for _ in range(i):
        timmy.rt(angle)
        timmy.fd(100)


screen = Screen()
screen.exitonclick()
