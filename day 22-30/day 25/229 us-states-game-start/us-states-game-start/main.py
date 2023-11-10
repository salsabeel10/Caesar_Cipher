import turtle
import pandas

tim=turtle.Turtle()
tim.penup()
tim.hideturtle()

df=pandas.read_csv("day 25/229 us-states-game-start/us-states-game-start/50_states.csv")
screen= turtle.Screen()
screen.title("USA Map")

img="/home/salsabeel/Desktop/Python-udemy/day 22-31/day 25/229 us-states-game-start/us-states-game-start/blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
correct=0
count=0
corrected_list=[]
df["state"]=df["state"].str.lower()

while count<=50:
    gussed_state=screen.textinput(title=f"{correct}/50 State Correct", prompt="What's the State Name")
    if gussed_state == None:
        break
    
    result = df[df['state']== gussed_state.lower()]

    if not result.empty and gussed_state not in corrected_list:
        state_name = result['state'].values[0].capitalize()
        corrected_list.append(gussed_state)
        correct+=1
        x=result['x'].values[0]
        y=result['y'].values[0]
        tim.goto(x,y)
        tim.write(state_name,align="center",font=("Arial", 10, "normal"))
    count+=1
print(corrected_list)
screen.exitonclick()

