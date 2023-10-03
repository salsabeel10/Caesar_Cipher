import turtle as t

tim=t.Turtle()

def mv_forward():
    tim.forward(10)

def mv_backward():
    tim.backward(10)

def mv_right():
    tim.right(10)

def mv_left():
    tim.left(10)

def Clear():
    tim.reset()

screen=t.Screen()
screen.listen()

screen.onkey(key="w",fun=mv_forward)
screen.onkey(key="s",fun=mv_backward)
screen.onkey(key="a",fun=mv_left)
screen.onkey(key="d",fun=mv_right)
screen.onkey(key="c",fun=Clear)

screen.exitonclick()