for i in range(1,101):
  if i%3==0 and i%5==0:
    print("Fizz Bizz",i)  
  elif i%5==0:
    print("Bizz",i)
  elif i%3==0:
    print("Fizz",i)  
  else:
    print(i)