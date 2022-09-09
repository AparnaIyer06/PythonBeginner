#Dictionary Methods 

#Removing Dictionary Items

#Removing an Item by key and return its value

D={"Name":"Bob","Age":25,"Job":"Development"}
x=D.pop("Age")
print(D)#{"Name":"Bob","Age":25,"Job":"Development"}
#Removed Value
print(x)#25 (Only the removed value is printed)

#Removing an Item from the dictionary
D={"Name":"Bob","Age":25,"Job":"Development"}
del D["Age"]
print(D) #{"Name":"Bob","Job":"Development"}


#Copy and popitem() methods

fruits={"a":"apple","o":"orange","m":"mango","k":"kiwi"}
print("Dictionary: ",fruits)
new_fruits=fruits.copy()
print(new_fruits)
del(new_fruits["m"])
print(new_fruits)
print(fruits)
newfruits1=fruits
del(newfruits1["a"])
print(newfruits1,"\n",fruits)


Cars = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = Cars.popitem()#Pops out the last item in the dictionary
#An item represents the key-value pair.
print(x)  #year: 1964


#Nested Dictionaries
Dict={1:"Geeks",2:"For",3:{"1":"Good day","2":"to","3": "one and all."}}
print(Dict[3]["2"])

     
#Pretty Printing a Dictionary
import json
Winners={"Nihar":3,"Rohan":5,"Zeba":3,"Roshan":1,"James":5}
print(json.dumps(Winners,indent=4)) #Parameters: Dictionary_Name, Indent

#Deleting a Dictionary
del Dict
print(Dict)

