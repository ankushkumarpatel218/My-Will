import sqlite3
from prettytable import PrettyTable
con = sqlite3.connect("employee.db")
cur = con.cursor()


def show_all_employee():
    print("********************************\n"
          "Show All Employee in the Company:\n"
          "********************************")
    sql = "select * from employee"
    cur.execute(sql)
    res = cur.fetchall()
    len1 = len(res)
    header = ['Department_no', 'Employee_Name', 'EmployeeID', 'Role',
              'Employee_City', 'Salary', 'Date_of_birth', 'Phone_Number','Gender']
    table = PrettyTable(header)
    for i in res:
        res = list(i)
        table.add_row(res)
        
    print(f"the Total number of employee in the company: {len1}")
    print(table)    