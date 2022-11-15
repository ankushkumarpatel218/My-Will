import sqlite3
con = sqlite3.connect("employee.db")
cur = con.cursor()


def promote_emp():
    print("*************************\n"
          "Promotion of an Employee:\n"
          "*************************")
    emp_id = input("Enter The Employee Id ( 4-Digits ): E").strip()
    dept = input("Enter the Employee Department Number ( 2-Digit ): D").strip()
    sql = f"select * from Employee where EmployeeID = 'E{emp_id}' and Department_no = 'D{dept}'"
    cur.execute(sql)
    res = cur.fetchall()
    len1 = len(res)
    if len1 == 1:
        new_role = input("Enter the new role of the employee: ").title().strip()
        promote = f"""update Employee set role = '{new_role}'
                    where EmployeeID = 'E{emp_id}' and Department_no = 'D{dept}'"""
        cur.execute(promote)
        con.commit()
        print(f"\nEmployee E{emp_id} has been promoted to {new_role}!\n")

    else:
        print(f"\nThere is no employee with empID {emp_id} in the company!\n")

