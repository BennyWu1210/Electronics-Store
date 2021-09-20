from tkinter import *

# TODO:
#  1. A username textfield
#  2. A password textField
#  3. A registration button
#  4. A submit button


def login_screen(window):
    text = Label(window, height=10, width=50, text="Login Screen", bg="red")
    entry = Entry(window)
    # text.grid(row=110, column=100)

    text.place(x=int(window.winfo_width()/2), y=int(window.winfo_height()/8))


