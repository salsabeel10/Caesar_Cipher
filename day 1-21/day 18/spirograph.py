import turtle as t
import random
tom=t.Turtle()
t.colormode(255)
tom.pensize(1)
tom.speed('fastest')
r=100

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    tup=(r,g,b)
    return tup

for i in range(72):
    k=(i+1)*5
    tup=random_color()
    tom.color(tup)
    tom.circle(r)
    tom.setheading(k)

my=t.Screen()
my.exitonclick()
