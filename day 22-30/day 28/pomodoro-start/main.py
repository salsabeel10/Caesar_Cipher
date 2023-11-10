import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps=0
    window.after_cancel(timer)
    canvas.itemconfig(timer_txt,text="00:00")
    timer_label.config(text="Timer")
    check.config(text="")
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    
    if reps % 8 == 0:
        timer_label.config(text="Long",fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        
        timer_label.config(text="Short",fg=PINK)
        count_down(short_break_sec)
        
    else:
        timer_label.config(text="Work",fg=GREEN)
        count_down(work_sec)
        
        



    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min=math.floor(count / 60)
    count_sec=count%60
    if count_sec<10:
        count_sec = f"0{count_sec}"
        

    canvas.itemconfig(timer_txt,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer=window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks=""
        for _ in range(math.floor(reps/2)):
            marks +="✔"
            check.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Promodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME, 35,"bold"))
timer_label.grid(row=0,column=1)

canvas=Canvas(width=205, height=224, bg=YELLOW, highlightthickness=0)
tomato_img=PhotoImage(file="day 28/pomodoro-start/tomato.png")
canvas.create_image(103,112,image=tomato_img)
timer_txt=canvas.create_text(115, 133, text="00:00", fill="white", font=(FONT_NAME, 33,"bold"))
canvas.grid(row=1,column=1)



start=Button(text="Start",highlightthickness=0,command=start_timer)
start.grid(row=2,column=0)

reset=Button(text="Reset",highlightthickness=0,command=reset_timer)
reset.grid(row=2,column=2)

check=Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME, 30,"bold"))
check.grid(row=3,column=1)

window.mainloop()
