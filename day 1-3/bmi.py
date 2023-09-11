weight=int(input("enter Your weight in Kg: "))
hight=float(input("enter your hight in cm: "))
bmi=round(weight/(hight/100)**2,2)


if bmi<18.5:
    print(f"You're Bmi {bmi} and Under Weight")
elif bmi>=18.5 and bmi<25:
    print(f"You're Bmi {bmi} and Normal Weight")
elif bmi>=25 and bmi<30:
    print(f"You're Bmi {bmi} and Over Weight")
elif bmi>=30 and bmi<35:
    print(f"You're Bmi {bmi} and Obese")
else:
    print(f"You're Bmi {bmi} and clinically Obeseity")