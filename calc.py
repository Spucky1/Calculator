import tkinter as tk
from tkinter import ttk




window = tk.Tk()
window.geometry("1920x1080")

def shuntingyard(): 
    textbox_text= textbox.get()
    rpn=[]
    output = []
    for i in textbox_text:
        print(i.isdigit())
        if i.isdigit() == True:
                rpn.append(i)
        elif i == "+" or i == "-" or i == "*" or i == "/":
                output.append(i)

    rpn += output
    print(rpn)
  
    print(textbox_text)
    return(rpn, output)
#No entiend que es postfix pero el nombre es chevre
def postfix(rpn, ouput):
      
      
   
textbox =ttk.Entry()
button = tk.Button(window,text="print",command= shuntingyard)
textbox.pack()
lbl =tk.Label(window, text="")
lbl.pack(pady=10)
button.pack()
window.mainloop()
