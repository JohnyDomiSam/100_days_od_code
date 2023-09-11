from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.score = 0
        self.penup()
        self.write_score()

    def write_score(self):
        self.goto(0, 250)
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER.", align="center", font=FONT)
        self.goto(0, -30)
        self.write(f"Your final score is {self.score}.", align="center", font=FONT)
