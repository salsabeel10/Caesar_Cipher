from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    df=pd.read_csv("to_learn.csv")
except FileNotFoundError:
    df=pd.read_csv("flash-card-project-start/data/french_words.csv")
    
list_of_words = df.to_dict(orient='records')


def next_card():
    global flip_timer,current_card
    window.after_cancel(flip_timer)
    current_card=choice(list_of_words)
    #french
    word_french=current_card["French"]
    canvas.itemconfig(canvas_image,image=card_front)
    canvas.itemconfig(title_txt, text="French",fill="black")
    canvas.itemconfig(translate_txt, text=word_french,fill="black") 
    flip_timer=window.after(3000, func=flip_card)
    

    

    
    


def flip_card():
    #english
    word_english=current_card["English"]
    canvas.itemconfig(canvas_image,image=card_back)
    canvas.itemconfig(translate_txt, text=word_english,fill="#fff")
    canvas.itemconfig(title_txt, text="English",fill="#fff")
    
def remove_card():
    list_of_words.remove(current_card)
    new_df=pd.DataFrame(list_of_words)
    new_df.to_csv("to_learn.csv",index=False)
    next_card()
    
    




window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=window.after(3000,flip_card)

canvas=Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front=PhotoImage(file="flash-card-project-start/images/card_front.png")
card_back=PhotoImage(file="flash-card-project-start/images/card_back.png")
canvas_image=canvas.create_image(412,265,image=card_front)
title_txt=canvas.create_text(400, 150, text="French", fill="black", font=("ariel", 40,"italic"))
translate_txt=canvas.create_text(400, 265, text="Traue", fill="black", font=("amiri", 50,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

right_img=PhotoImage(file="flash-card-project-start/images/right.png")
wrong_img=PhotoImage(file="flash-card-project-start/images/wrong.png")
wrong_btn=Button(image=wrong_img,highlightthickness=0,command=next_card)
right_btn=Button(image=right_img,highlightthickness=0,command=remove_card)
wrong_btn.grid(row=1,column=0)
right_btn.grid(row=1,column=1)

next_card()
window.mainloop()
