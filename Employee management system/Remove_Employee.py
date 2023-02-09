import sqlite3
con = sqlite3.connect("employee.db")
cur = con.cursor()

def remove_emp():
    print("*********************\n"
          "Remove Employee Data:\n"
          "*********************")
    emp_id = input("Enter The Employee Id ( 4-Digits ): E").strip()
    dept = input("Enter the Employee Department Number ( 2-Digit ): D").strip()
    sql = f"select * from Employee where EmployeeID = 'E{emp_id}' and Department_no = 'D{dept}'"
    cur.execute(sql)
    res = cur.fetchall()
    len1 = len(res)
    if len1 == 1:
        remove = f"""delete from Employee where EmployeeID = 'E{emp_id}' and Department_no = 'D{dept}'"""
        cur.execute(remove)
        con.commit()
        print("\nThe Book Data Has Been Removed!\n")

    else:
        print(f"\nThere is no employee with empID E{emp_id} in the company!\n")









