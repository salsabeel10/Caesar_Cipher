
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
PATH="day 24/218 Snake-Project-Code-from-Day-21/data.txt"

with open(PATH,mode="r") as file:
    c=file.read()
    
old_high=int(c) 

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score=old_high
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
        new_high=self.high_score
        with open(PATH,mode="w") as file:
            file.write(str(new_high))
        self.score=0
        self.update_scoreboard()
    
    


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
