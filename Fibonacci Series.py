#First n numbers in Fibonacci Series
no_of_terms=int(input("Enter the number of terms of the Fibonacci series: "))
num1=0
num2=1
print(num1)
print(num2)
for i in range(3,no_of_terms+1):
    Sum=num1+num2
    print(Sum)
    num1=num2
    num2=Sum
    
