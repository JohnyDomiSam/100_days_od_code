import turtle
from turtle import Turtle
import pandas as pd
import time


screen = turtle.Screen()
writer = Turtle(visible=False)
screen.title("US State guessing game")
IMAGE = "blank_states_img.gif"
screen.addshape(IMAGE)
turtle.shape(IMAGE)
turtle.tracer(0)
data = pd.read_csv("50_states.csv")
data_list = data["state"].to_list()
guess_list = []
score = 0

while len(guess_list) < 50:
    time.sleep(0.1)
    screen.update()
    answer_state = screen.textinput(
        title=f"{score}/50 states correct.", prompt="What's another state's name ?"
    ).title()

    if answer_state == "Exit":
        states_to_learn = [state for state in data_list if state not in guess_list]
        frame = pd.DataFrame(states_to_learn, columns=["states to learn"])
        frame.to_csv("States_to_learn.csv")
        break

    elif answer_state in guess_list:
        print("You already guesseed this one, guess again !")
    elif answer_state in data_list:
        right_answer = data[data.state == answer_state]
        writer.penup()
        writer.goto(int(right_answer.x), int(right_answer.y))
        writer.write(answer_state)
        guess_list.append(answer_state)
        score += 1
screen.mainloop()
