from turtle import Turtle,Screen

class Draw():
    def __init__(self) -> None:
        self.timy=Turtle()
    def shape(self,side,color):
        self.timy.color(color)
        angle=360/side

        for _ in range(side):
            self.timy.forward(100)
            self.timy.right(angle)

drawer=Draw()

drawer.shape(3,"black")
drawer.shape(4,"red")
drawer.shape(5,"blue")
drawer.shape(6,"green")
drawer.shape(7,"yellow")
drawer.shape(8,"orange")
drawer.shape(9,"pink")
drawer.shape(10,"gold")






my_screen=Screen()
my_screen.exitonclick()