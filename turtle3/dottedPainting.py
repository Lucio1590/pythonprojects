import colorgram
from turtle import Turtle, Screen
from random import randint, choice

t = Turtle()
t.pensize(20)
t.speed(0)
s = Screen()
s.colormode(255)
t.penup()
t.ht()
colors = colorgram.extract('spots.jpeg', 20)

rows = 7
cols = 7

t.setpos(-s.screensize()[0], -s.screensize()[1])

for i in range(rows):
    for j in range(cols):
        color = choice(colors).rgb
        rgb = (color.r, color.g, color.b)
        print(rgb)
        t.pencolor(rgb)
        t.dot()
        t.forward(100)
    t.setpos(-s.screensize()[0], t.pos()[1]+100)

Screen().exitonclick()