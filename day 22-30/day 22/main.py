from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorebord import Scoreboard
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle=Paddle(370,0)
l_paddle=Paddle(-370,0)
ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")



game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect paddle
    if ball.distance(r_paddle)< 50 and ball.xcor() > 350 or ball.distance(l_paddle)< 50 and ball.xcor() < -350:
        ball.bounce_x()

    #right paddle miss
    if ball.xcor() > 390:
        ball.reset_postion()
        scoreboard.l_point()
        
        
    #left paddle miss    
    if ball.xcor() < -390:
        ball.reset_postion()
        scoreboard.r_point()
      
        


screen.exitonclick()