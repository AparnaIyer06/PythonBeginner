#Dictionaries:Practice Programs 

ODD={1.0:"One",3.0:"Three",5.0:"Five",7.0:"Seven",9.0:"Nine"}
print(ODD.keys())
for i in ODD:
    print(i)
for i in ODD:
    print(i,":",ODD[i])
print(ODD.values())
print(ODD.items()) #Prints items of the dictionary as a list of tuples
print(len(ODD))
print(7.0 in ODD)#True
print(2.0 in ODD)#False 
print(ODD.get(9.0))
del ODD[9.0]
print(ODD)
