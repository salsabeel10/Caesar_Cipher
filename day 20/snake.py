from turtle import Turtle

MOVE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake():
    def __init__(self):
        self.squares=[]
        self.create_snake()
        self.head=self.squares[0]

    def create_snake(self):
        for i in range(3):
            tim=Turtle(shape='square')
            tim.penup()
            tim.color("white")
            tim.goto(x=i*20*-1,y=0)
            self.squares.append(tim)
    
    def move(self):
        for seg_num in range(len(self.squares)-1,0,-1):
            new_x=self.squares[seg_num-1].xcor()
            new_y=self.squares[seg_num-1].ycor()
            self.squares[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE) 
    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() !=UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() !=LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)