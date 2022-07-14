from cProfile import label
from tkinter import *
from turtle import left, title
root=Tk()
root.title("Hello!!!MotherF")
root.geometry("444x233")
title_label= Label(text='''India, officially the Republic of India (Hindi: Bhārat Gaṇarājya),[26] is a country in South Asia.
\nIt is the seventh-largest country by area, the second-most populous country, and the most populous democracy in the world.
\nBounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast,
\nit shares land borders with Pakistan to the west;[f] China, Nepal, and Bhutan to the north; and Bangladesh and Myanmar to the east.
\nIn the Indian Ocean, India is in the vicinity of Sri Lanka and the Maldives; 
\nits Andaman and Nicobar Islands share a maritime border with Thailand, Myanmar and Indonesia.''',
bg="red",fg="white",padx=44,pady=40,font="comicsansms 12 bold",borderwidth=3,relief=SUNKEN)
title_label.pack(side=LEFT,anchor="sw",fill=Y)
root.mainloop()