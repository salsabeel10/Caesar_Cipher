# import colorgram
import turtle as t
import random

# # Extract 6 colors from an image.
# colors = colorgram.extract('/home/salsabeel/Desktop/Python-udemy/day 18/172 hirst-painting-start/image.jpg', 10)

# list=[]
# for color in colors:
#     r,g,b=color.rgb
#     one=(r,g,b)
#     list.append(one)
    
    
# print(list)
color_list=[(202, 164, 110), (236, 219, 223), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20)]
t.colormode(255)
tim=t.Turtle()

tim.shapesize(1.2)
tim.hideturtle()
tim.penup()
spacing=50
for row in range(10):
    for col in range(10):
        
        tim.goto(col * spacing - 200, row * spacing - 200)
        tim.dot(20,random.choice(color_list))
        




my_screen=t.Screen()
my_screen.exitonclick()