from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Pridá entry z polí Website, Email/Username, Password
    a uloží ich do textového súboru."""
    get_website = entry_website.get()
    get_email = email_entry.get()
    get_password = entry_password.get()
    with open("29.Password_manager_app/data.txt", "a") as data:
        data.write(f"{get_website} | {get_email} | {get_password}\n")
    entry_password.delete(0, END)
    entry_website.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="29.Password_manager_app/logo.png")
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
def generate_password():
    print("Generate_password buttin clicked")


password_button = Button(text="Generate Password", command=generate_password, width=15)
password_button.grid(column=2, row=3)


# Button Add

add_button = Button(text="Add", highlightthickness=0, command=save, width=44)
add_button.grid(column=1, row=4, columnspan=2)

# Entry Website
entry_website = Entry(width=51)
entry_website.insert(END, string="Enter your email here")
entry_website.focus()
entry_website.grid(column=1, row=1, columnspan=2)

# Entry Email/Username
email_entry = Entry(width=51)
email_entry.insert(END, string="Enter your email here.")
email_entry.grid(column=1, row=2, columnspan=2)

# Entry Password
entry_password = Entry(width=32)
entry_password.insert(END, string="Enter your password here.")
entry_password.grid(column=1, row=3)


window.mainloop()
