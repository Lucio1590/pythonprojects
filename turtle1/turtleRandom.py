from turtle import Turtle, Screen
from random import randint, choice
t = Turtle()
angles = [0, 90, 180, 270]
go = True
t.pensize(12)
t.speed(0)
Screen().colormode(255)

while go:
    t.setheading(choice(angles))
    t.forward(30)
    new_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    t.color(new_color)
