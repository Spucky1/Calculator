import tkinter as tk
from tkinter import ttk
window =tk.Tk()
window.geometry("1920x1080")

def inFixToPostFix():
    textbox_text = textbox.get()
    queue = []
    #This is a fifo data stucture
    stack = []
    #This is a Lifo data stucture
    inFixExpression = textbox_text.split()
    if inFixExpression[0] x
        
#  postfix evalutation to work with values and stack givn from shutting


textbox =ttk.Entry()
button = tk.Button(window,text="Click me please", command=inFixToPostFix)
textbox.pack()
lbl =tk.Label(window, text="")
lbl.pack(pady=10)
button.pack()
window.mainloop()