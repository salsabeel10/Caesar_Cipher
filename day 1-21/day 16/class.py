class User:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
        self.place="kerala"
        self.follwers=0
        self.following=0
    def follow(self,user):
        self.following +=1
        user.follwers +=1



user1=User("salsabeel",22)
user2=User("alhad",20)

user1.follow(user2)

print(f"user1 following:{user1.following}\n user1 followers:{user1.follwers} ")
print(f"user2 following{user2.following}\n user2 followers{user2.follwers}")