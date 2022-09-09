#Program to compute area of circle
radius=float(input("Enter the radius of the circle\n: "))
area_circle=3.14*radius**2
print("The area of the circle is: ",area_circle)

#Program to compute area of triangle
a=float(input("Enter first side of triangle:\n"))
b=float(input("Enter second side of triangle:\n"))
c=float(input("Enter third side of triangle:\n"))
s=(a+b+c)/2
area_tri=(s*(s-a)*(s-b)*(s-c))**0.5
print(s)
print("The area of triangle is: ",area_tri)
print("The area of triangle is: %0.3f"%area_tri)
if type(area_tri)==complex:
    print("Invalid values entered.")
    
    
