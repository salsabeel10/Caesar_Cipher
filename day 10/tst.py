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

for value in operation:
    print(value)