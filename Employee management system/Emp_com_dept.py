import sqlite3
from prettytable import PrettyTable
con = sqlite3.connect("employee.db")
cur = con.cursor()


def com_dept_emp():
    print("*************************************\n"
          "Show Employees with Common Department:\n"
          "*************************************")
    dept = input("Enter the Employee Department Number ( 2-Digit ): D").strip()
    sql = f"select * from Employee where Department_no = 'D{dept}'"
    cur.execute(sql)
    res = cur.fetchall()
    len1 = len(res)
    header = ['Department_no', 'EmployeeID', 'Employee_Name', 'Role',
              'Employee_City', 'Salary', 'Date_of_birth', 'Phone_Number','Gender']
    table = PrettyTable(header)
    for i in res:
        table.add_row(i)
    print(f"The Number of Employees in Department D{dept} = {len1}")
    print(table)






