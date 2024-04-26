from turtle import Turtle, Screen
from random import randint, choice
screen = Screen()
screen.colormode(255)
screen.setup(width=500, height=400)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
input_correct = False
bet = ""
while not input_correct:
    bet = screen.textinput("Race a bet", f"What color do you think will win?\nAvailable Colors: {colors}")
    if bet in colors:
        input_correct = True

turtles = [Turtle() for x in range(0, len(colors))]
print(turtles)
for i, t in enumerate(turtles):
    t.color(colors[i])
    t.shape("turtle")
    t.penup()
    t.goto(-230, i*20-60)
winner = None
go = True
while go:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winner = turtle
            go = False
            break
        else:
            turtle.forward(randint(5, 20))

if winner.pencolor() == bet:
    print(f"You've won! The winner is: {winner.pencolor()}")
else:
    print(f"You've lost! The winner is: {winner.pencolor()}")

screen.exitonclick()
