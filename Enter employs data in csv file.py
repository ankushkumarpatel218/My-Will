import prettytable
import csv
import pandas

EmpID = []
EName = []
Salary = []
DeptID = []
Gender = []

Data = {"EmpID": EmpID, "EName": EName, "Salary": Salary, "DeptID": DeptID, "Gender": Gender}

while True:
    ID = input("Enter Employ Id: ")
    Name = input("Enter Employ Name: ").title()
    salary = float(input("Enter Employ Salary: "))
    deptId = input("Enter Employ Department Id: ")
    gender = input("Enter Employ's Gender ( M / F ): ").upper()

    EmpID.append(ID)
    EName.append(Name)
    Salary.append(salary)
    DeptID.append(deptId)
    Gender.append(gender)

    if input("Wanna Quit? Press * : ") == "*":
        break
    else:
        continue

df = pandas.DataFrame(Data)
df.to_csv("Emp.csv", index=False)

csvfile = open("Emp.csv", 'r', newline='')
read = csv.reader(csvfile)

header = next(read)
table = prettytable.PrettyTable(header)
for i in read:
    table.add_row(i)
print(table)
