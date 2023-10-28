import random

student=["alhad","salsabeel","salman","ehfat"]

mark_dict={name:random.randint(10,100) for name in student}

print(mark_dict)

passed_stud={name:mark for (name,mark) in mark_dict.items() if mark > 60}

print(passed_stud)