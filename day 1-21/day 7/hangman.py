import random
import req


life_img=req.stages
print(req.logo)
#1
print(life_img[6])
word_lists=req.word_list


chosen_word=random.choice(word_lists)

len=len(chosen_word)
lives=6

display=[]
for i in range(len):
    display.append("_")

#2
end_of_game=False
gussed_list=[]
while not end_of_game:
    guess=input("Guess a Letter:").lower()
    print("\033c")
    if guess in display:
        print("You Already Guessed that letter \n\n Guess another Letter\n\n")
        print(display)
        continue
    found=False
    for j in range(len):
        letter=chosen_word[j]
        if guess==letter:
            display[j]=letter
            found=True
    gussed_list.append(guess)
    print(display)
    if not found:
        
        print(f"You Gussed Wrong Letter {guess}\n")
        
        lives-=1

        print(life_img[lives])
        if lives==0:
            print(f"You Lose The correct Word:{chosen_word}")
            end_of_game=True
    
            
        
                  
    
    if "_" not in display:
        end_of_game=True
        print("Congragulation.. You won")
        
        