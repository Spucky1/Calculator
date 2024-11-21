import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("1920x1080")
def printInput(): 
    inp = textbox.get(1.0, "end-1c") 
    lbl.config(text = "Provided Input: "+inp) 

textbox =ttk.Entry(command= printInput)
button = tk.Button(text=("hello"), command= printInput)

textbox.pack()
lbl =tk.Label(window, text="")
lbl.pack()
button.pack()
window.mainloop()
