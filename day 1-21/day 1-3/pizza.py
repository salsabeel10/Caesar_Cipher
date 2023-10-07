print("Welcome to Pizza Hut")
size=input("Select Size: S, M, or L:")
pepperoni=input("Do You want pepperoni? Y or N:")
cheese=input("Do You want Extra Cheese? Y or N:")

price=0

if size=='s':
    price+=15
elif size=='m':
    price+=20
elif size=='l':
    price+=25

if (pepperoni=='y' and cheese =='y') and (size=='s'):
    price+=3
elif(pepperoni=='y' and cheese =='y'):
    price+=4

elif (pepperoni=='y' and cheese =='n'):
    price+=3
elif (pepperoni=='n' and cheese =='y'):
    price+=1

print(f"Your total price is {price} ")    