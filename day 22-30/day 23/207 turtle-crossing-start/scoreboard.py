from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.current_lvl=0
        self.penup()
        self.goto(x=-280,y=260)
        self.level()
        
    
    def game_over(self):
        self.goto(x=0,y=0)
        self.write("Game Over",align="center",font=FONT)
        
    def level(self):
        self.clear()
        self.current_lvl+=1
        self.write(f"Level: {self.current_lvl}",align="left",font=FONT)
