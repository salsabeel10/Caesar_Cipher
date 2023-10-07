def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

def mod(n1,n2):
    return n1%n2

operation={
    add:"+",
    sub:"-",
    mul:"*",
    div:"/",
    mod:"%"
}

flag=True
while True:
    num1=float(input("Enter First Number:"))
    while flag:
        operation=input("Choose a Operation \n+\n-\n*\n/\n%\nPick up An Operation:")
        num2=float(input("Enter Next Number:"))

        
        
        result=round(result,2)
        print(f"{num1} {operation} {num2} = {result}")

        choice=input("Do You want to Continue with the Result [Y/N]").lower()
        if choice=='y':
            num1=result
        else:
            flag=False
        
    restart=input("Do You Want to Restart [Y/N]").lower()
    if restart!='y':
        print("exit")
        break
    else:
        print("\033c", end='')