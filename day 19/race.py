from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make the Bet",prompt="Which Turtle Will win:")
colors=["red","blue","yellow","green","pink","brown"] 
is_race_on=False
# tim=Turtle(shape="turtle")
# tom=Turtle(shape="turtle")
# timy=Turtle(shape="turtle")
# tomy=Turtle(shape="turtle")
# time=Turtle(shape="turtle")
# tam=Turtle(shape="turtle")

# tim.penup()
# tim.goto(x=-235,y=0)
# tim.color(random.choice(colors))
# tom.goto(x=-235,y=40)
# tom.color(random.choice(colors))
turtles=[]
for i in range(1,7):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i-1])
    new_turtle.goto(x=-235,y=-130+(i*40))
    turtles.append(new_turtle)
    
if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor()>240:
            win_color=turtle.pencolor()
            
            is_race_on=False
            break
            
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)


if user_bet==win_color:
    print(f"Congragulation {user_bet} Turtle Won ")
else:
    print(f"Sorry You Lose, {win_color} Turtle Won")

screen.exitonclick()