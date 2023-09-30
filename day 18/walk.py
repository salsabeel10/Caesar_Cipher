import turtle as t 
import random
timy=t.Turtle()

t.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    tup=(r,g,b)
    return tup

timy.pensize(15)
timy.speed("fastest")
for _ in range(200):
    direction=random.choice([0,90,270,180])
    tup=random_color()
    timy.color(tup)
    timy.forward(25)
    timy.setheading(direction)
    
    
    

screen=t.Screen()
screen.exitonclick()