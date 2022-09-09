#To check whether a given element is present in a list or not
List=eval(input("Enter a list of integers: "))
num=int(input("Enter the number to be searched: "))
position=-1
for i in range(0,len(List)):
    if num==List[i]:
        position+=1
if position==-1:
    print("Number",num,"is not present in the list.")
else:
    print("Number", num,"is present in the list at position",List.index(num))
