from turtle import Turtle


AlIGNMENT=('CENTER')
FONT=("Times New Roman", 14, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto(0, 280) 
        self.point=0
        self.update_scorebord()
       
        
    def update_scorebord(self):
         self.write(f"Score : {self.point}",False,align=AlIGNMENT,font=FONT)


    def add(self,num):
        
        self.point+=num
        self.clear()
        
        self.update_scorebord()
        