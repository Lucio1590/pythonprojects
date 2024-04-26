from turtle import Turtle, Screen
from random import randint
circles = 100
angle = 360/circles

turtle = Turtle()
turtle.speed(0)
Screen().colormode(255)


for i in range(circles):
    turtle.circle(100)
    turtle.right(angle)
    new_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    turtle.color(new_color)
