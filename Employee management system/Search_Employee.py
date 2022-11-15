import sqlite3
from prettytable import PrettyTable
con = sqlite3.connect("employee.db")
cur = con.cursor()


def search_emp():
    print("****************************\n"
          "Search for an Employee Data:\n"
          "****************************")
    emp_id = input("Enter The Employee Id ( 4-Digits ): E").strip()
    dept = input("Enter the Employee Department Number ( 2-Digit ): D").strip()
    sql = f"select * from Employee where EmployeeID = 'E{emp_id}' and Department_no = 'D{dept}'"
    cur.execute(sql)
    res = cur.fetchall()
    len1 = len(res)
    header = ['Department_no', 'Employee_Name', 'EmployeeID', 'Role',
              'Employee_City', 'Salary', 'Date_of_birth', 'Phone_Number','Gender']
    table = PrettyTable(header)
    if len1 == 1:
        for i in res:
            table.add_row(i)
        print(table)

    else:
        print(f"\nThis employee with empID E{emp_id} is not in the company!\n")

