from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xcor_inc = 5
        self.ycor_inc = 5
        self.sleeping_time = 0.05

    def move(self):
        new_x = self.xcor() + self.xcor_inc
        new_y = self.ycor() + self.ycor_inc
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.ycor_inc *= -1

    def bounce_x(self):
        self.xcor_inc *= -1
        self.sleeping_time *= 0.9
