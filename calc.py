from tkinter import*
from tkinter import ttk

window = Tk()
window.geometry("1920x1080")
def printInput(): 
    inp = textbox.get(1.0, "end-1c") 
    lbl.config(text = "Provided Input: "+inp) 

textbox =ttk.Entry()
button = Button(text=("hello"))

textbox.pack()
lbl =Label(Frame, Text="")
lbl.pack()
button.pack()
window.mainloop()
