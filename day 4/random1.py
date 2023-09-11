import random

user_seed=int(input("Enter a Seed Number:"))
random.seed(user_seed)



friend=input("enter the Names of Your Friends each seprate by ',':")

name=friend.split(",")
length=len(name)
print(length)
k=random.randint(0,length-1)
selected=name[k]

print(f"Today {selected} is selected to Give the Bill")