from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✓"
REPS = 0
TIMER = None


# ---------------------------- FOCUS WINDOW FUNCTION ------------------------------- #
def focus_window(option):
    if option == "on":
        window.deiconify()
        window.focus_force()
        window.attributes('-topmost', 1)
        window.bell()
    elif option == "off":
        window.attributes('-topmost', 0)


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global REPS
    window.after_cancel(TIMER)
    REPS = 0
    timer_label.config(text="Timer", fg=RED)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")
    start_button.config(state="normal")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60
    start_button.config(state="disabled")
    if REPS % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_seconds)
        focus_window("on")
    elif REPS % 2 != 0:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
        focus_window("off")
    elif REPS % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_seconds)
        focus_window("on")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    min = count // 60
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"

    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(10, count_down, count - 1)
    else:
        start_timer()
        if REPS % 2 == 0:
            checkmark_label.config(text=CHECKMARK * (int(REPS / 2)))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

# Timer label
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25, "bold"))
timer_label.grid(column=1, row=0)

# Checkmark label
checkmark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
checkmark_label.grid(column=1, row=3)

# Start button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Reset button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
