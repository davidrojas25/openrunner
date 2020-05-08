from tkinter import *

root = Tk()
root.title("Simple Calculator")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()
    
e = Entry(root, width=50, bg = "yellow", fg = "blue", borderwidth = 5)
e.pack()
e.insert(0, "Enter Your Name: ")
myButton = Button(root, text="Enter Your Name:", command=myClick)
myButton.pack()



root.mainloop()