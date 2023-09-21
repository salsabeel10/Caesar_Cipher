from random import randint,choice 
import art
from game_data import data


def random_item():
    ran_num=choice(data)

    name = ran_num['name']
    follower_count = ran_num['follower_count']
    description = ran_num['description']
    country = ran_num['country']
    return name,follower_count,description,country



print(art.logo)
name,follower_count,description,country=random_item()
a_count=follower_count
print(f"Compare A: {name}, a {description} from {country}")

print(art.vs)

name,follower_count,description,country=random_item()
b_count=follower_count
print(f"Compare B: {name}, a {description} from {country}")

ans=input("Who has More Follwers? Type 'A' or 'B':")