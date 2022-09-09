#To print the element of minimum value in a list and its index position
List= eval(input("Enter a list: "))

Smallest= List[0]
Index=0
for i in range(1,len(List)):
    if List[i]<Smallest:
        Smallest=List[i]
        Index=i
print("Smallest integer: ",Smallest, "is at index",Index)

Greatest= List[0]
Index=0
for i in range(1,len(List)):
    if List[i]>Greatest:
        Greatest=List[i]
        Index=i
print("Greatest integer: ",Greatest, "is at index",Index)


#Sum of elements in a list
Sum=0
Count=0
for i in range(0,len(List)):
    Sum=Sum+List[i]
    Count+=1
print("The sum of elements in the list is ",Sum," and there are",Count,"elements.")    
print("The mean is: ",Sum/len(List))


