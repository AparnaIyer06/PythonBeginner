#Dictionary Program (Fruits_Colours)
Dict_Fruits={"Apple":"Red","Guava":"Pink","Muskmelon":"Orange"}
print("The original dictionary is: ",Dict_Fruits)
fruit=input("Enter the new fruit: ")
colour=input("Enter the color of the fruit: ")
Dict_Fruits[fruit]=colour
print("The updated dictionary is: ",Dict_Fruits)

#Concatenate two dictionaries
import json
Dict1={"1":"Soccer","2":"Basketball","3":"Baseball","4":"Golf"}
Dict2={"A":"Monopoly","B":"Chinese Checkers","C":"Chess","D":"Ludo"}
Dict3={}
for d in(Dict1,Dict2):
    Dict3.update(d)
print("Concatenated dictionary: ",json.dumps(Dict3,indent=2))

#To check if a given key already exists in a dictionary
Dict={1:"Physics",2:"Chemistry",3:"Maths"}
Key=int(input("Enter the key that is to be searched: "))
if Key in Dict:
    print(Key,"is present in ",Dict)
else:
    print(Key,"is not present in ",Dict)

#To create a dictionary where the keys are numbers and the values are the squares of the keys
Squares=dict()
for i in range(5):
   Squares[i]=i**2
print(Squares)
#To sum up all the items in a dictionary
Dict={"Data1":1,"Data2":2,"Data3":3}
R=sum(Dict.values())
print(R)

#Nested Dictionaries
#Example 1
People={1: {"Name":"John","Age":"27","Sex":Male,2:{"Name":"Mary","Age":"28","Sex":"Female"}}
print(People)
#Example 2
Employee={"John":{"Age":25,"Salary":2000},"Diya":{"Age":35,"Salary":2500}}
for key in Employee:
        print("Employee: ",key)
        print("Age: ",Employee[key]["Age"])
        print("Salary:",Employee[key]["Salary"])
       
              
