name=input("Enter Your Name:")
friend=input("Enter Your Friend Name:")

#lower case
f=friend.lower()
n=name.lower()

t=n.count('t')
r=n.count('r')
u=n.count('u')
e=n.count('e')
l=n.count('l')
o=n.count('o')
v=n.count('v')
e=n.count('e')

perT=t+r+u+e
perL=l+o+v+e

t=f.count('t')
r=f.count('r')
u=f.count('u')
e=f.count('e')
l=f.count('l')
o=f.count('o')
v=f.count('v')
e=f.count('e')
perT+=t+r+u+e
perL+=l+o+v+e


per1=str(perT)
per2=str(perL)

pers=per1+per2

per=int(pers)




if per<10 or per>=90:
    print(f"You're score is {per} and You are coke and mentos")
elif per>=40 and per>=50:
    print(f"You're score is {per} and You guys ok")
else:
    print(f"You're score is {per}")

