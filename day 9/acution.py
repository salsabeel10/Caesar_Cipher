import art
name_dict={}
print(art.logo)
flag=True


while flag:
    name=input("What is Your Name:")
    amound=int(input("What's your Bid? $"))
    name_dict[name]=amound
    next=input("is there any other Biders [Y/N]").lower()
    if next=="n":
        flag=False
        break
    print("\033c", end='')
    

max_amound=0
for person,amount in name_dict.items():
    if amount>max_amound:
        max_amound=amount
        max_person=person
print("\033c", end='')

print(f"{max_person} has won bid with ${max_amound}")