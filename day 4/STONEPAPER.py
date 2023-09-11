import random
rock = '''
    Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    Scissor
    ______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game=[rock,paper,scissors]

user_no=int(input("for Rock 1, Paper 2, Scissor 3:"))

user_no-=1
print("*****YOU*****")
print(game[user_no])

computer=random.randint(0,3)
computer-=1
print("*****Computer*****")
print(game[computer])
#Rock 0 Paper 1 Scissor 2
if user_no==computer:
    print("game Draw")
elif user_no==1 and computer==2:
    print("Computer Won You Lose")
elif user_no==0 and computer==1:
    print("Computer Won You Lose")
elif user_no==2 and computer==0:
    print("Computer Won You Lose")
else:
    print("You Won Congragulation ")