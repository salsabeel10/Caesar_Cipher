import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

alpha=[]
numra=[]
symbol=[]



#for alphabet
for i in range(nr_letters):
   i=random.randint(0,51)
   alpha.append(letters[i])


#for numbers
for j in range(nr_numbers):
   j=random.randint(0,9)
   numra.append(numbers[j])


#for symbol
for k in range(nr_symbols):
   k=random.randint(0,7)
   symbol.append(symbols[k])



password=alpha+numra+symbol
random.shuffle(password)
new_password=''.join(password)
print("Your Strong Password:",new_password)