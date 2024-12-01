import tkinter as tk
from tkinter import ttk
import nltk
nltk.download('punkt_tab')


window = tk.Tk()
window.geometry("1920x1080")
Operators = ["+","-","/","*"]
def printInput(): 
    textbox_text= textbox.get()
    tolkeins = nltk.word_tokenize(textbox_text)
    for i in tolkeins:
         print(i.isdigit())
    print(tolkeins)
    if Operators in tolkeins:
        print("true")
    lbl.config(text = textbox_text) 

textbox =ttk.Entry()
button = tk.Button(window,text="print",command= printInput)
textbox.pack()
lbl =tk.Label(window, text="")
lbl.pack(pady=10)
button.pack()
window.mainloop()
