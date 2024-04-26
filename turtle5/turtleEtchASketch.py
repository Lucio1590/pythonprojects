from turtle import Turtle, Screen
t = Turtle()
screen = Screen()
go = True
t.speed(0)


def forward():
    t.forward(10)


def backward():
    t.backward(10)


def turn_right():
    t.right(-10)


def turn_left():
    t.left(-10)


def go_home():
    t.home()


def clear_screen():
    go_home()
    t.clear()


screen.listen()

screen.onkey(forward, 'w')
screen.onkey(backward, 's')
screen.onkey(turn_right, 'a')
screen.onkey(turn_left, 'd')
screen.onkey(clear_screen, 'c')
screen.mainloop()


