from tkinter import *
root=Tk()
root.title("Dainik Bhaskar")
root.geometry("1080x1920")
photo=PhotoImage(file="dog.png")
sandeep_label = Label(image=photo)
text_label = Label(text="Kutte TEri  amma  ki chut",bg="red",font="comicsansms 12 bold")
text_label.pack()
sandeep_label.pack()

root.mainloop()