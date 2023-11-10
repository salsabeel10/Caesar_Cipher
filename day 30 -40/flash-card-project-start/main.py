from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas=Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front=PhotoImage(file="flash-card-project-start/images/card_front.png")
canvas.create_image(412,265,image=card_front)
language_txt=canvas.create_text(400, 150, text="French", fill="black", font=("ariel", 40,"italic"))
french_txt=canvas.create_text(400, 263, text="Traue", fill="black", font=("ariel", 60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

right_img=PhotoImage(file="flash-card-project-start/images/right.png")
wrong_img=PhotoImage(file="flash-card-project-start/images/wrong.png")
wrong_btn=Button(image=wrong_img,highlightthickness=0)
right_btn=Button(image=right_img,highlightthickness=0)
wrong_btn.grid(row=1,column=0)
right_btn.grid(row=1,column=1)

window.mainloop()
