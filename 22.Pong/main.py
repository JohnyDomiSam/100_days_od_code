from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

tim = Turtle(shape="classic", visible=False)
tim.color("white")
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-390, 0))
r_paddle = Paddle((380, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(l_paddle.up, "Up")
screen.onkey(l_paddle.down, "Down")
screen.onkey(r_paddle.up, "w")
screen.onkey(r_paddle.down, "s")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.sleeping_time)
    ball.move()

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()
        ball.move()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 365 or ball.distance(l_paddle) < 50 and ball.xcor() < -375:
        ball.bounce_x()
        ball.move()
    if ball.xcor() > 365:
        ball.goto(0, 0)
        ball.bounce_x()
        ball.sleeping_time = 0.5
        scoreboard.l_point()
    if ball.xcor() < -375:
        ball.goto(0, 0)
        ball.bounce_x()
        ball.sleeping_time = 0.05
        scoreboard.r_point()


screen.exitonclick()
