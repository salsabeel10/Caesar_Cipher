from random import choice
import art
from game_data import data
import os

def clear_console():
    os.system('clear')

def random_item():
    ran_num = choice(data)
    index = data.index(ran_num)

    name = ran_num['name']
    follower_count = ran_num['follower_count']
    description = ran_num['description']
    country = ran_num['country']
    return name, follower_count, description, country, index

def compare(a, b, ans):
    if a > b:
        result = 'a'
    elif b > a:
        result = 'b'
    elif a==b:
        return True
    else:
        return False

    return ans == result

score = 0


print(art.logo)

while True:
    name_a, follower_count_a, description_a, country_a, index_a = random_item()
    name_b, follower_count_b, description_b, country_b, index_b = random_item()

    print(f"Compare A: {name_a}, a {description_a} from {country_a}")
    print(art.vs)
    print(f"Compare B: {name_b}, a {description_b} from {country_b}")
    print(f"a:{follower_count_a}, b:{follower_count_b}")
    ans = input("Who has More Followers? Type 'A' or 'B':").lower()

    if compare(follower_count_a, follower_count_b, ans):
        score += 1 
        clear_console()
        print(art.logo)
        print(f"Congragulation.. Your Score is {score}")
        
    else:
        print(f"Wrong answer. Your final score is {score}")
        break
