#To display the frequency of a character in a list
'''
List1=eval(input("Enter a list: "))
char=int(input("Enter the element whose frequency is to be determined: "))
count=0
a=-1
for i in range(0,len(List1)):
    if char==List1[i]:
        count+=1
        a+=1
        break
if a==0:
    print("The frequency of",char,"in the list is",count)
else:
    print(char,"is not available in the list.")
'''


#To display the frequency of a character in a list 
List1=eval(input("Enter a list: ")) 
char=int(input("Enter the element whose frequency is to be determined: ")) 
counter=0 

for i in range(0,len(List1)): 
    if char==List1[i]: 
        counter+=1 
if counter==0: 
    print(char,"is not available in the list.") 
else: 
    print("Frequency of",char,"in the list is",counter,".") 
