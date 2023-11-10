from tkinter import *

window=Tk()
window.title("Miles to KM")
window.config(padx=20,pady=20)

def btn_click():
    result=float(input.get())
    mile=round((result*1.609),2)
    km.config(text=mile)

    


input=Entry(width=7)
input.grid(column=1, row=0)

my_label=Label(text="Miles")
my_label.grid(column=2,row=0)

my_label=Label(text="is equal to")
my_label.grid(column=0,row=1)

km=Label(text="0")
km.grid(column=1,row=1)

my_label=Label(text="Km")
my_label.grid(column=2,row=1)

button=Button(text="Calculate",command=btn_click)
button.grid(column=1,row=3) 

window.mainloop()