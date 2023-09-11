import time
from turtle import Screen
from food import Food
from snake import Snake
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    score_board.update_scoreboard()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.score += 1
        score_board.update_scoreboard()

    # Detect collision with wall
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        score_board.score_reset()
        snake.snake_reset()
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.score_reset()
            snake.snake_reset()

screen.exitonclick()
