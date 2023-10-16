from turtle import Turtle
import random as r
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        self.all_cars=[]
        self.car_speed= STARTING_MOVE_DISTANCE
        


    def create_car(self):
        random_chance = r.randint(1,6)
        if random_chance ==1:
            new_car=Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(r.choice(COLORS))
            random_y=r.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)
    
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def move_inc(self):
            self.car_speed+=MOVE_INCREMENT
            
            
