from turtle import Turtle,Screen

timy=Turtle()

timy.shape("turtle")
for _ in range(4):
    timy.forward(100)
    timy.left(90)

my_screen=Screen()
my_screen.exitonclick()