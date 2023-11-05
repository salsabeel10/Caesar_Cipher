from tkinter import *

def btn_click():
    txt=input.get()
    my_label.config(text=txt)
    print(txt)

window=Tk()
window.title("Hello")
window.minsize(width=500, height=300)
#label
my_label=Label(text="this is label",font=("Arial",24,"bold"))
my_label.grid(column=0,row=0)

#button 
button=Button(text="Click Me 1",command=btn_click)
button.grid(column=1,row=1)

button=Button(text="Click Me 2",command=btn_click)
button.grid(column=2,row=0) 

#entry
input=Entry(width=10)
input.grid(column=3, row=2)

 




window.mainloop()