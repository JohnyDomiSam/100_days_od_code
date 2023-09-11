import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

num_of_loops = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move()
    num_of_loops += 1
    if num_of_loops % 6 == 0:
        car.create_cars()
    # detekcia kolízie s autom
    for new_car in car.all_cars:
        if player.distance(new_car) < 25:
            scoreboard.game_over()
            game_is_on = False

    # detekcia hráča s cieľovou súradnocou
    if player.ycor() > 280:
        car.increase_move_speed()
        scoreboard.increase_score()
        player.set_to_start()

screen.exitonclick()
