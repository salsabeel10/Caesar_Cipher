import turtle

screen= turtle.Screen()
screen.title("US Map")

img="/home/salsabeel/Desktop/Python-udemy/day 22-31/day 25/229 us-states-game-start/us-states-game-start/blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

ans_state=screen.textinput(title="Guess The State", prompt="What's the State Name")
print(ans_state)

screen.exitonclick()