from tkinter import *
import csv
from tkinter.filedialog import *
from input import *
from main import *

root = Tk()
text=Text(root)
def call():
    file = askopenfilename()
    image=input(file)
    text.insert(INSERT,main(image))
    text.pack()
b=Button(root,text="Input image",command=call)
b.pack()
root.mainloop()