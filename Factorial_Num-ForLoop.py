#Factorial of a number
factorial=1
num=int(input("Enter a number: "))
for i in range(1,num+1):
    factorial=factorial*i
print(num,"! =",factorial)
