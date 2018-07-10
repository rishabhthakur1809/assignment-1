#Question1
from tkinter import *
root = Frame()
root.pack()
d = {"rahul": 323, "prink": 321, "vijay": 126, "qwert": 789, "mnbv": 987, "wert": 565, "rajiv": 127,
     "anip": 256}

w1 = Label(root, text="Name =")
w1.pack(side="bottom")
w2 = Label(root, text="Phone Number =")
w2.pack(side="top")

lst = Listbox(root)
sbar = Scrollbar(root)
sbar.config(command=lst.yview)
lst.config(yscrollcommand=sbar.set)
sbar.pack(side=RIGHT, fill=Y)
lst.pack(side=LEFT, expand=YES, fill=BOTH)
#Question2
def handleList(event):
    label = lst.get(ACTIVE)
    print(label)
    ph = d.get(label)
    global w1, w2
    w1.config(text=label)
    w2.config(text=ph)


lst.bind('<Double-1>', handleList)


for k, v in d.items():
    lst.insert('end', k)

root.mainloop()