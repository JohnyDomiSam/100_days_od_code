from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- SEARCH ENGINE ------------------------------- #
def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            website = entry_website.get()
            if website in data:
                messagebox.showinfo(
                    title="Info",
                    message=f'You already have password for {website}: {data[website]["password"]}',
                )
            else:
                messagebox.showinfo(
                    message="No details for the website exists.", title="Warning"
                )
    except FileNotFoundError:
        messagebox.showinfo(message="No password saved yet.", title="Error")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)
    entry_password.delete(0, END)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Pridá entry z polí Website, Email/Username, Password
    a uloží ich do textového súboru."""
    get_website = entry_website.get()
    get_email = email_entry.get()
    get_password = entry_password.get()
    new_data = {get_website: {"email": get_email, "password": get_password}}

    if len(get_website) == 0 or len(get_email) == 0 or len(get_password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please don't leave any fields empty !"
        )
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        entry_password.delete(0, END)
        entry_website.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Label Website
website_label = Label(text="Website:", font=("courier", 10, "bold"))
website_label.grid(column=0, row=1)

# Label Email/Username
email_label = Label(text="Email/Username:", font=("courier", 10, "bold"))
email_label.grid(column=0, row=2)

# Label Password
password_label = Label(text="Password:", font=("courier", 10, "bold"))
password_label.grid(column=0, row=3)


# Button Password
password_button = Button(text="Generate Password", command=generate_password, width=15)
password_button.grid(column=2, row=3)


# Button Add
add_button = Button(text="Add", highlightthickness=0, command=save, width=44)
add_button.grid(column=1, row=4, columnspan=2)


# Entry Website
entry_website = Entry(width=32)
entry_website.insert(END, string="Enter your website here")
entry_website.focus()
entry_website.grid(column=1, row=1)

# Button Search
search_button = Button(
    text="Search", highlightthickness=0, command=find_password, width=15
)
search_button.grid(column=2, row=1)

# Entry Email/Username
email_entry = Entry(width=51)
email_entry.insert(END, string="Enter your Email/Username here.")
email_entry.grid(column=1, row=2, columnspan=2)

# Entry Password
entry_password = Entry(width=32)
entry_password.grid(column=1, row=3)


window.mainloop()
