from random import randint,choice 
import art
from game_data import data


def random_item():
        ran_num=choice(data)
        index=data.index(ran_num)

        name = ran_num['name']
        follower_count = ran_num['follower_count']
        description = ran_num['description']
        country = ran_num['country']
        return name,follower_count,description,country,index

def compare(a,b,ans):
    if a>b:
          result='a'
    elif b>a:
          result='b'
    else:
          return False
    return ans==result
         

score=0

print(art.logo)
name,follower_count,description,country,A_index=random_item()
a=follower_count
print(f"Compare A: {name}, a {description} from {country}")

print(art.vs)

name,follower_count,description,country,B_index=random_item()
b=follower_count
print(f"Compare B: {name}, a {description} from {country}")
print(f"A:{a},B:{b}")

ans=input("Who has More Follwers? Type 'A' or 'B':").lower()
highest=compare(a,b,ans)

while highest:
      score+=1
      print(F"Your Score is {score}")
      name,follower_count,description,country,B_index=random_item()
      print(f"Compare A: {name}, a {description} from {country}")
      ans=input("Who has More Follwers? Type 'A' or 'B':").lower()
      highest=compare(a,b,ans)