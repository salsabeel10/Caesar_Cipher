from turtle import Turtle
import random

FOODSIZE=0.7

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=FOODSIZE, stretch_wid=FOODSIZE)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        

    def refresh(self):
        random_x=random.randint(-276,276)
        random_y=random.randint(-276,276) 
        self.goto(x=random_x,y=random_y)