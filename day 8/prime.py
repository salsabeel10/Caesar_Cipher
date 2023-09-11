def prime(num):
    count=1
    if num<=1:
        print(f"the given number {num} is not considerd as prime ")
    else:
        num_c=int(num/2)+1
        for i in range(2,num_c):
            if num%i==0:
                count+=1
    if count==1:
        print(f"the given {num} is prime")
    else:
        print(f" {num} is not prime")
num=int(input("Enter a Number"))
prime(num)
