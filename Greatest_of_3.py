#To print greatest of 3 numbers
num1=float(input("Enter Number 1: "))
num2=float(input("Enter Number 2: "))
num3=float(input("Enter Number 3: "))
if num1>num2:
    if num1>num3:
        print(num1," is the greatest.")
    else:
        print(num3," is the greatest.")
elif num2>num1:
    if num2>num3:
        print(num2," is the greatest.")
    else:
        print(num3, "is the greatest.")
