#BMI Calculator
weight=float(input("Enter your weight in kg: "))
height=float(input("Enter your height in m: "))
BMI=weight/(height**2)
if BMI<=18.5 and BMI>0:
    status='underweight'
elif BMI<=25 and BMI>18.5:
    status='normal weight'
elif BMI<=30 and BMI>25:
    status='overweight'
elif BMI>30:
    status='obese'
else:
    print("Invalid weight or height entered.")
print("Your BMI is: %3.2f"%BMI)
print("This indicates:",status,".")
