from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, coordinates: tuple = ...):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(coordinates)

    def up(self):
        if self.ycor() <= 240:
            self.setheading(90)
            self.forward(20)

    def down(self):
        if self.ycor() > -240:
            self.setheading(270)
            self.forward(20)
