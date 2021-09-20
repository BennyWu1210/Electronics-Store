# Graphical User Interface using Tkinter

from tkinter import *
from GUI.login_screen import *

window = Tk()

window.title("Welcome to Benny's Electronics' store")
screen_width = int(window.winfo_screenwidth() * 0.6)
screen_height = int(window.winfo_screenheight() * 0.78)

window.geometry(str(screen_width) + "x" + str(screen_height))
window.update()
# login screen

login_screen(window)
window.mainloop()




