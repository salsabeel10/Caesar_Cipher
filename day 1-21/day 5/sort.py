
student_score = input("Input a list of student heights ").split()
for n in range(0, len(student_score)):
  student_score[n]=int(student_score[n])
 
largest=student_score[0]

for i in student_score:
  if i>largest:
    largest=i

print(largest)

