#DictionaryEmployeesSalaries
n=int(input("Enter the number of employees: "))
DictEmployeeSalary=dict()
for i in range(1,n+1):
    name=input("Enter the name of the employee: ")
    salary=input("Enter the salary of the employee: ")
    DictEmployeeSalary[name]=salary
for i,j in DictEmployeeSalary.items():
    print("Name: ",i,"Salary:",j)
