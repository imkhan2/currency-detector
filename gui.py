from tkinter import *
import csv
from tkinter.filedialog import *
from input import *
from main import *

root = Tk()
root.title("Currency Detector")
root.minsize(width=500,height=500)
root.configure(background="LIGHT BLUE")
var=StringVar()
label=Label(root,textvariable=var,relief=RAISED,bg="BLUE",fg="WHITE",font=('Helvetica','24','bold'))
var.set("CURRENCY RECOGNITION SYSTEM")
label.pack()
var2= StringVar()
var2.set("Answer")
def call():
    file = askopenfilename()
    image=input(file)
    var2.set(main(image))
b=Button(root,text="Input image",command=call,bg="BLUE",fg="WHITE")
b.place(relx=.5, rely=.4, anchor="c")
label2 = Label(root, textvariable=var2, relief=RAISED, bg="PURPLE", fg="WHITE", font=('Helvetica', '24', 'bold'))
label2.place(relx=.5, rely=.6, anchor="c")
root.mainloop()