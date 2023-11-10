import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player= Player()
car_manager= CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()

    #Detect Collition

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on=False
            score.game_over()
        #sucessfull 
                                    if player.is_starting():
            player.goto_start()
            car_manager.move_inc()
            score.level()


screen.exitonclick()
