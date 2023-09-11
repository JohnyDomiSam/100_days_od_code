from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.create_cars()
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        new_car = Turtle(shape="square", visible=False)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.goto(300, random.randint(-240, 240))
        new_car.setheading(180)
        new_car.showturtle()
        self.all_cars.append(new_car)

    def move(self):
        for new_car in self.all_cars:
            new_car.forward(self.move_speed)

    def increase_move_speed(self):
        self.move_speed += MOVE_INCREMENT
