MENU = {
    "tea": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 15,
    },
    "coffe": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 100,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def show_resource():
    for key,value in resources.items():
        print(f"{key}: {value}")

def order(choice):
    
    if choice in MENU:
        drink=MENU[choice]
        ingrediant=drink['ingredients']
        cost=drink['cost']


    print(f"drink:{drink}\ningrediant:{ingrediant}\ncost:{cost}")


while True:
    choice = input("What Would You like? (tea/cofee/cappuccino):").lower()

    if choice=='report':
        show_resource()
    elif choice in ["tea","cofee","cappuccino"]:
        order(choice)
    elif choice=="off":
        break
    else:
        print("Wrong Command")
