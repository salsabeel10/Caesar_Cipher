# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
sum=0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  len=n+1
  sum=int(sum+student_heights[n])
print(len)
result=sum/len
print(round(result))
#Write your code below this row 👇




