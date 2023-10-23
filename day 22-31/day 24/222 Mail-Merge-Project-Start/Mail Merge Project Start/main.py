with open("day 24/222 Mail-Merge-Project-Start/Mail Merge Project Start/Input/Names/invited_names.txt",mode="r") as file:
    names=file.read().splitlines()



with open("day 24/222 Mail-Merge-Project-Start/Mail Merge Project Start/Input/Letters/starting_letter.txt",mode="r") as files:
     tex=files.read()
          
for name in names:
     text=tex.replace("[name]",name)
     with open(f"/home/salsabeel/Desktop/Python-udemy/day 22-31/day 24/222 Mail-Merge-Project-Start/ReadyToSend/to_{name}.txt",mode="w")as filed:
        filed.write(text)
     