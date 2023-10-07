from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
screen.listen()
score=Scoreboard()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect food
    if snake.head.distance(food) < 16:
        food.refresh()
        snake.extend()
        score.add(1)
    
    #detect Collition
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on=False
        score.game_over()

    #detect collition on tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)< 10:
            game_is_on=False
            score.game_over()

screen.exitonclick()


