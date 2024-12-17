import tkinter as tk
from tkinter import ttk
# outline is if i = "+" and stack(-1) = "power" or stack(-1) = "*" or stack(-1) = 


window = tk.Tk()
window.geometry("1920x1080")

def shuntingyard(): 
    textbox_text= textbox.get()
    queue=[]
    stack = []
    if stack == []:
         print("w")
    #Problem is that output[-1] does not exist
    for i in textbox_text:
        print(i.isdigit())
        if i.isdigit() == True:
                queue.append(i)
        elif i ==  "*":
                if stack == []:    
                    print("worki")
                    if stack[-1] == "^":
                        queue.append(stack.pop())
                        stack.append(i)
                        print("works")
                    else:
                         stack.append(i)
        elif i == "/":
            if stack == []:
                if stack[-1] == "*" or stack[-1] == "^":
                    queue.append(stack.pop())
                    stack.append(i)
                else:
                    stack.append(i)
        elif i == "+":
            if stack == []:
                if stack[-1] == "*" or stack[-1] == "/" or stack[-1] == "^":
                    queue.append(stack.pop())
                    stack.append(i)
                else:
                    stack.append(i)
        elif i =="-":
            if stack == []:
                if stack[-1] == "*" or stack[-1] == "/" or stack[-1] == "+" or stack[-1] =="^":
                    queue.append(stack.pop())
                    stack.append(i)
                else:
                     stack.append(i)
                
              
                
                

    print(stack)
    queue += stack
    print(queue)
  
    print(textbox_text)
    return(queue, stack)
#Postfix eval no lo e hecho

      
      
   
textbox =ttk.Entry()
button = tk.Button(window,text="print",command= shuntingyard)
textbox.pack()
lbl =tk.Label(window, text="")
lbl.pack(pady=10)
button.pack()
window.mainloop()
