import tkinter as tk
from tkinter import ttk




window = tk.Tk()
window.geometry("1920x1080")


def printInput(): 
    textbox_text= textbox.get()
    for i in textbox_text:
        queue = []
        stack = []
        print(i.isdigit())
        if i.isdigit() == True:
            i.append(queue)
        elif i == "(" or i == "*" or i =="/" or i =="+" or i ==  "-" or i ==")":
             i.append(stack)
    for I in stack: 
        if I == "*" & I == "+" or I == "-" or I == "/" or I == "(":
                I.append(queue)
        elif I == "/" & I != "*" or I ==  "+" or I == "-" or I == "(":
                I.append(queue)
        elif I == "+" & I != "*" or I != "/" or I == "-" or I  == "(":
                I.append(queue)
        elif I == "-" & I != "*" or I != "/" or I !="+" or I =="(":
            if I == "-":
                I.append(queue)
        


                    


           
        
            
        
            

    print(queue)

    print(textbox_text)
   

textbox =ttk.Entry()
button = tk.Button(window,text="print",command= printInput)
textbox.pack()
lbl =tk.Label(window, text="")
lbl.pack(pady=10)
button.pack()
window.mainloop()
