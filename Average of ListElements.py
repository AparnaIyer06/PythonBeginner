#To compute the mean of elements in a list
List=eval(input("Enter a list: "))
Sum=0
Count=0
for i in range(0,len(List)):
    Sum+=List[i]
    Count+=1
Average=Sum/Count
print("The mean of elements in the list is:%0.2f"%Average)
