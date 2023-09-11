from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter a color: ")
while user_bet not in colors:
    print(f'You entered "{user_bet}", which is not a correct color. Try again.')
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter a color: ")
all_turtles = []
y_coordinate = -100
for i in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.up()
    turtle.goto(x=-230, y=y_coordinate)
    y_coordinate += 40
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            turtle.shapesize(2, 2)
            turtle.home()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost. The {winning_color} turtle won.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
