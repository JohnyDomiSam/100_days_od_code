from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=300)
window.config(padx=50, pady=100)

# Label1 = "Miles" grid 2, 0
my_label = Label(text="Miles", font=("Aerial", 14, "bold"))
my_label.grid(column=2, row=0)

# Label2  = "is qual to" grid 0, 1
label2 = Label(text="is equal to", font=("Aerial", 14, "bold"))
label2.grid(column=0, row=1)

# Label3  =  "calculation in kms" grid 1, 1
label3 = Label(text="0", font=("Aerial", 14, "bold"))
label3.grid(column=1, row=1)

# Label4  = "km" grid 2, 1
label2 = Label(text="km", font=("Aerial", 14, "bold"))
label2.grid(column=2, row=1)

# Entry grid 2, 0
input_window = Entry(width=10)
input_window.grid(column=1, row=0)


# Button grid 1, 2
def button_clicked():
    """Miles to kms conversion"""
    km = round((float(input_window.get()) / 0.621371192), 2)
    label3.config(text=km)


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
