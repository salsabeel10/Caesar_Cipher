student_mark={
    "salsabeel":91,
    "alhad":88,
    "ehfat":76,
    "messi":64,
    "boss":10
}

student_grade={}

for name in student_mark:
    if student_mark[name]>=90:
        student_grade[name]="Outstanding"
    elif student_mark[name]>=80:
        student_grade[name]="Excelent"
    elif student_mark[name]>=70:
        student_grade[name]="Good"
    elif student_mark[name]>=60:
        student_grade[name]="Average"
    elif student_mark[name]<50:
        student_grade[name]="Failed"

for name in student_grade:
    print(f"{name} : {student_grade[name]}")
    