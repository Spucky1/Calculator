import tkinter as tk
from tkinter import ttk




window = tk.Tk()
window.geometry("1920x1080")
OPPS = "+-*/"
def printInput(): 
    textbox_text= textbox.get()
    for i in textbox_text:
        rpn = []
        print(i.isdigit())
        if i.isdigit() == True:
            rpn.append(i)
            
        
            

    print(rpn)

    print(textbox_text)
   

textbox =ttk.Entry()
button = tk.Button(window,text="print",command= printInput)
textbox.pack()
lbl =tk.Label(window, text="")
lbl.pack(pady=10)
button.pack()
window.mainloop()
