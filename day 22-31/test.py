def add(*args):
    sum=0
    for n in args: 
        sum+=n
    return sum

res=add(2,3,5,12)
print(res)