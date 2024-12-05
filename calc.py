import tkinter as tk
from tkinter import ttk




window = tk.Tk()
window.geometry("1920x1080")
OPP = ["+","-","*","/"]
def printInput(): 
    textbox_text= textbox.get()
    for i in textbox_text:
        rpn = []
        print(i.isdigit())
        for k in textbox_text:
            if k.isdigit() == True:
                rpn.append(k)
           
        for OPPS in textbox_text:
            if  OPP in OPPS:
             rpn.append(OPPS)
            
        
            

    print(rpn)

    print(textbox_text)
   

textbox =ttk.Entry()
button = tk.Button(window,text="print",command= printInput)
textbox.pack()
lbl =tk.Label(window, text="")
lbl.pack(pady=10)
button.pack()
window.mainloop()
