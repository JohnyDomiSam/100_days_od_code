from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
DICT = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
data_list = data.to_dict(orient="records")


# -------------------- Cards function -------------------------
def know_answer():
    next_card()
    data_list.remove(DICT)
    data_frame = pd.DataFrame(data_list)
    data_frame.to_csv("data/words_to_learn.csv", index=False)


# -------------------- Buttons function -----------------------
def next_card():
    global DICT, TIMER
    window.after_cancel(TIMER)
    DICT = choice(data_list)
    canvas.itemconfig(canvas_image, image=old_image)
    canvas.itemconfig(trans_text, text=DICT["French"], fill="black")
    canvas.itemconfig(language_text, text="French", fill="black")
    TIMER = window.after(5000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=new_image)
    canvas.itemconfig(trans_text, text=DICT["English"], fill="white")
    canvas.itemconfig(language_text, text="English", fill="white")


# --------------------------- UI ------------------------------

# Master window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
TIMER = window.after(5000, flip_card)
# Canvas
canvas = Canvas(
    master=window, bg=BACKGROUND_COLOR, width=800, height=526, highlightthickness=0
)
old_image = PhotoImage(file="images/card_front.png")
new_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=old_image)


language_text = canvas.create_text(
    400, 150, text="French", font=(FONT_NAME, 40, "italic")
)
trans_text = canvas.create_text(
    400, 263, text="Translation", font=(FONT_NAME, 60, "bold")
)
canvas.grid(column=0, row=0, columnspan=2)

# right Button
right_image = PhotoImage(file="images/right.png")
yes_button = Button(image=right_image, highlightthickness=0, command=know_answer)
yes_button.grid(column=1, row=1)
# wrong Button
wrong_image = PhotoImage(file="images/wrong.png")
yes_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
yes_button.grid(column=0, row=1)

next_card()

window.mainloop()
