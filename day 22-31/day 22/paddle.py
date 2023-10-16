from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,xcor,ycor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.penup()
        self.goto(x=xcor,y=ycor)


    

    def up(self):
        y=self.ycor() + 20#current y cordinate
        self.goto(self.xcor(),y)

    def down(self):
        y=self.ycor() - 20
        self.goto(self.xcor(),y)