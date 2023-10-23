dog_age=float(input("enter Your dog age:"))

if dog_age > 2:
    new_age=dog_age-2
    human_age=new_age*4+21
else:
    human_age=dog_age*10.5

print(f"Your Dog age In Human years :{human_age}")