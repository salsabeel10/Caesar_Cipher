def paint(h,w,c):
    can_=round((h*w)/c)
    print(f"You Will need {can_} cans")



hight=int(input("Height of Wall:"))
width=int(input("width of Wall:"))
coverage=5
paint(h=hight,w=width,c=coverage)