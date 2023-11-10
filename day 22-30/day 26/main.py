#name to upper using list comprehension
# names=["salsabeel","alhad","ehfat","thasnim"]

# new_name=[n.upper() for n in names if len(n) >= 5]

# print(new_name) 

#sqaure of numbers
# numbers=[1,1,2,3,5,8,13,21,34,55]

# new_list=[n*n for n in numbers]

# print(new_list)

#even numbers

numbers=[1,1,2,3,5,8,13,21,34,55]

new_list=[n for n in numbers if n%2==0]

print(new_list)