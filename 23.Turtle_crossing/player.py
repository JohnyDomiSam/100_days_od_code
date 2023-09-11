from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(
        self, shape: str = "turtle", undobuffersize: int = 1000, visible: bool = True
    ) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.set_to_start()

    def set_to_start(self):
        self.color("black")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def up(self):
        self.forward(MOVE_DISTANCE)
