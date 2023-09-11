from turtle import Turtle

SCORE_FONT = ("Arial", 12, "normal")
TEXT_ALIGNMENT = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.score = 0
        self.high_score = int(self.read_data())

    def update_scoreboard(self):
        self.clear()
        self.pendown()
        self.write(
            f"Score is: {self.score} High score is: {self.high_score}",
            move=False,
            align=TEXT_ALIGNMENT,
            font=SCORE_FONT,
        )

    def score_reset(self):
        if self.score > self.high_score:
            self.update_highscore()
            self.high_score = self.score
        self.score = 0

    def read_data(self):
        with open("data.txt", mode="r") as data:
            data_written = data.read()
            return data_written

    def update_highscore(self):
        with open("data.txt", mode="w") as data1:
            data1.write(str(self.score))
