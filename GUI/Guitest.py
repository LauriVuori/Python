from tkinter import *

from tkinter.ttk import *
#Fill drop menus
Vals = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)


#First select button



def select():
    Rsel = Rms.get()
    txt = "Selected: " + Rsel
    lbl = Label(window, text=txt)
    lbl.grid(column=0, row=1)


    Lsel = lmps.get()
    txt = "Selected: " + Lsel
    lbl = Label(window, text=txt)
    lbl.grid(column=0, row=3)

    txt = "R: ", Rsel , "L: ", Lsel
    lbl = Label(window, text=txt)
    lbl.grid(column=0, row=4)

def quit():
    print("quit")


    


window = Tk()
window.title("Testi")
window.geometry('350x200')
Rms = Combobox(window)
#Get info from txt file.. How many objects---> Vals
Rms['values']= Vals
Rms.current(0) #set the selected item
Rms.grid(column=0, row=0)
Nselect1 = Label(window, text="No selected")
Nselect1.grid(column=0, row=1)
isClicked = False
### Second drop down
lmps = Combobox(window)
lmps['values'] = Vals
lmps.current(0) #set the selected item
lmps.grid(column=0, row=2)
Nselect2 = Label(window, text="No selected")
Nselect2.grid(column=0, row=3)
btn = Button(window, text="Lock", command=select)

btn.grid(column=1, row=2)
exbtn = Button(window, text="Exit", command=quit)
exbtn.grid(column=3, row=7)

####
window.mainloop()
