import random

print("Welcome to Number Gussing Game")
print("I Guessed a number Between 1 to 100 Find it")
level=input("Choose Your Difficulty [Easy/Hard]:").lower()

if level=='easy':
    attempt=10
elif level =="hard":
    attempt=5
else:
    print("invalid Choice of Level")
    exit()

random_num=random.randint(1,100)
is_gussed=False
while attempt!=0:

    print(f"You have Left {attempt} attempts")
    num=int(input("Enter a Number:"))
    attempt-=1
    if num==random_num:
        is_gussed=True
        break
    elif num<random_num:
        print("Too Low")
    elif num>random_num:
        print("Too High")
    else:
        is_gussed=False
        break

if is_gussed==False:
    print(f"Sorry Your Guess was wrong, Ans is {random_num}")
else:
    print(f"Congragulation Your Guess was Right {random_num}")