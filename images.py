from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to Code")
root.iconbitmap("giticon.ico")

my_img = ImageTk.PhotoImage(Image.open("warriors xc2019.jpg"))
my_label = Label(image=my_img)
my_label.pack()




button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()







root.mainloop() 