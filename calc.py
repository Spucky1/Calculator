from tkinter import*
from tkinter import ttk

window = Tk()
window.geometry("1920x1080")


textbox =ttk.Entry()
button = Button(text=("hello"))
textbox.pack()
button.pack()
window.mainloop()
