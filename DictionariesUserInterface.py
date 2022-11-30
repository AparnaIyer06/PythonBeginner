'''WAP to create a dictionary with students' names as keys, and their phone numbers as values
Print the dictionary in sorted order
Display the name and corresponding phone number, if present in the dictionary.
If not present, add (append) the name and corresponding phone number to the dictionary.'''

Dict_Students_Numbers=dict()

#Obtaining students' names and the corresponding phone numbers from the user
#Appending these to the dictionary

n=int(input("Enter the number of students in the directory: "))

for i in range(0,n):

    student_name=input("Enter the name of the student: ")

    student_number=input("Enter the phone number of the student: ")

    if len(student_number)!=10:

        print("Invalid phone number entered. Please try again.")

        continue #Returns to the for loop

    Dict_Students_Numbers[student_name]=student_number #Updating the dictionary with key-value pairs


print("Dictionary of students' names and numbers: ",Dict_Students_Names)

print("\n")

#To sort the elements of the dictionary

sorted_Dict_Students_Numbers=dict() #Defining the dictionary

sorted_keys_Students_Numbers=sorted(Dict_Students_Numbers) #Sorts the keys of the dictionary

for key in sorted_keys_Students_Numbers: #Iterating through the sorted keys

    sorted_Dict_Students_Numbers[key]=Dict_Students_Numbers[key] #Updating the new dictionary


print("Sorted Dictionary: ",sorted_Dict_Students_Numbers)

print("\n")

#To search for a dictionary item by key, and to display it, if present.

#If the entered name is not a key in the dictionary, enable the user to add a phone number corresponding to it, to the dictionary


student_name_user=input("Enter the name of the student that is to be searched for in the dictionary: ")

if student_name_user in Dict_Students_Names.keys():

    print("The entered key",student_name_user,"is present in the dictionary.")

    print(student_name_user,": ",Dict_Students_Numbers[student_name_user])

else: #Appending the student name and phone number typed by the user to the dictionary

    print("The entered key",student_name_user,"is not present in the dictionary.")

    print("Adding it to the dictionary...")

    print("\n")
    
    user_number=input("Enter the phone number corresponding to",student_name_user,": ")

    Dict_Students_Numbers[student_name_user]=user_number #Updating the key-value pair to the dictionary

    print(Dict_Students_Numbers)

print("\n")

    
