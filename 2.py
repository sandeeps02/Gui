from importlib import import_module
from tkinter import *
from PIL import Image,ImageTk
img_root=Tk()

img_root.geometry("955x944")
# photo=PhotoImage(file="dog.png")
# for jpg images?\

image=Image.open("me.jpg")
photo=ImageTk.PhotoImage(image)
sandeep_label = Label(image=photo)
sandeep_label.pack()
img_root.mainloop()