import tkinter as tk
from tkinter import ttk
#if i = "+" and stack(-1) = "power" or stack(-1) = "*" or stack(-1) = 


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
        elif i ==  "*":
                if output:    
                
                    if output[-1] == "^":
                        rpn.append(output.pop())
                        output.append(i)
                    else:
                         output.append(i)
        elif i == "/":
            if output:
                if output[-1] == "*" or output[-1] == "^":
                    rpn.append(output.pop())
                    output.append(i)
                else:
                    output.append(i)
        elif i == "+":
            if output:
                if output[-1] == "*" or output[-1] == "/" or output[-1] == "^":
                    rpn.append(output.pop())
                    output.append(i)
                else:
                    output.append(i)
        elif i =="-":
            if output:
                if output[-1] == "*" or output[-1] == "/" or output[-1] == "+" or output[-1] =="^":
                    rpn.append(output.pop())
                    output.append(i)
                else:
                     output.append(i)
                
              
                
                

    print(output)
    rpn += output
    print(rpn)
  
    print(textbox_text)
    return(rpn, output)
#No entiend que es postfix pero el nombre es chevre

      
      
   
textbox =ttk.Entry()
button = tk.Button(window,text="print",command= shuntingyard)
textbox.pack()
lbl =tk.Label(window, text="")
lbl.pack(pady=10)
button.pack()
window.mainloop()
