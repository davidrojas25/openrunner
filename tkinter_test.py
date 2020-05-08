from tkinter import *

#def kilometers_to_miles(kilometers):
#  miles = 0.00
  # conversion factor
#  conv_fac = 0.621371
  # calculate miles
#  miles = kilometers * conv_fac
#  print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))
def myClick():
    myLabel4 = Label(root, text="Look! I clicked a Button!!")
    myLabel4.grid(row=3, column=3)
root = Tk()

# creating a Label Widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is David Rojas")
myLabel3 = Label(root, text="             ")
myButton = Button(root, text="Click Me!", command="myClick")

#shoving it onto the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)
myLabel3.grid(row=1, column=1)
myButton.grid(row=2, column=2)
root.mainloop()
#kilometers_to_miles(float(input("Enter value in kilometers: ")))