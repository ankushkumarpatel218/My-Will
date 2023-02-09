import sqlite3
from prettytable import PrettyTable
con = sqlite3.connect("employee.db")
cur = con.cursor()


def com_role_emp():
    print("*******************************\n"
          "Show Employees with common role:\n"
          "*******************************")
    role = input("Enter the role: ").title().strip()
    sql = f"select * from Employee where role = '{role}'"
    cur.execute(sql)
    res = cur.fetchall()
    len1 = len(res)
    header = ['Department_no', 'Employee_Name', 'EmployeeID', 'Role',
              'Employee_City', 'Salary', 'Date_of_birth', 'Phone_Number','Gender']
    table = PrettyTable(header)
    for i in res:
        table.add_row(i)
    print(f"The Number of Employees who are {role} = {len1}")
    print(table)






