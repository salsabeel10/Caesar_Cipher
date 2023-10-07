MENU = {
    "tea": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 15,
    },
    "coffee": {
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

def show_resources():
    """Display the current resources in the machine."""
    for item, quantity in resources.items():
        print(f"{item}: {quantity}")

def make_coffee(choice):
    """Prepare and serve the selected coffee."""
    drink = MENU[choice]
    ingredients = drink['ingredients']
    cost = drink['cost']

    # Check if there are enough resources to make the selected drink
    for item, quantity in ingredients.items():
        if resources[item] < quantity:
            print(f"Sorry, not enough {item} available.")
            return

    # Ask the user to insert money
    while True:
        money_inserted = float(input(f"Please insert ${cost}: "))
        if money_inserted < cost:
            print("Sorry, not enough money inserted.")
        else:
            break

    # Calculate change and update resources
    change = money_inserted - cost
    resources["money"] += cost
    for item, quantity in ingredients.items():
        resources[item] -= quantity

    print(f"Enjoy your {choice}! Here's your change: ${change:.2f}")

while True:
    choice = input("What would you like? (tea/coffee/cappuccino): ").lower()

    if choice == 'report':
        show_resources()
    elif choice in ["tea", "coffee", "cappuccino"]:
        make_coffee(choice)
    elif choice == "off":
        break
    else:
        print("Wrong command. Please choose from the menu.")
