import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title('tkinter testing')

frame = ttk.Frame(root, padding=5)

def clickMe():
    label.configure(text= 'Hello ' + name.get())


label = ttk.Label(root, text = "Enter Your Name")
label.grid(column = 0, row = 0)

name = tk.StringVar()
nameEntered = ttk.Entry(root, width = 15, textvariable = name)
nameEntered.grid(column = 0, row = 1)

button = ttk.Button(root, text = "Click Me", command = clickMe)
button.grid(column= 0, row = 2)

frame.grid(column=0, row=0)


root.mainloop()

