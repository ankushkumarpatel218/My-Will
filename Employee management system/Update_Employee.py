import sqlite3
con = sqlite3.connect("employee.db")
cur = con.cursor()


def update_emp():
    print("*********************\n"
          "Update Employee Data:\n"
          "*********************")
    emp_id = input("Enter The Employee Id ( 4-Digits ): E")
    dept = input("Enter the Employee Department Number ( 2-Digit ): D")
    sql = f"select * from Employee where EmployeeID = 'E{emp_id}' and Department_no = 'D{dept}'"
    cur.execute(sql)
    res = cur.fetchall()
    len1 = len(res)
    if len1 == 1:
        print("""        1.Employee name
        2.Department
        3.Employee city
        4.Employee's phone number
        5.Date of birth""")
        choice = input("Enter Which Data you want to update? ").strip()
        if choice == '1':
            emp_name = input("Enter the Correct Employee Name: ").title().strip()
            update = f"""update Employee set Employee_Name = '{emp_name}' 
                            where EmployeeID = 'E{emp_id}' and Department_no = 'D{dept}'"""
            cur.execute(update)
            con.commit()
            print(f"\nName of Employee E{emp_id} has been updated!\n")

        elif choice == '2':
            new_dept = input("Enter the Employee's New department: ").strip()
            update = f"""update Employee set Department_no = 'D{new_dept}' 
                                        where EmployeeID = 'E{emp_id}' and Department_no = 'D{dept}'"""
            cur.execute(update)
            con.commit()
            print(f"\nDepartment of Employee E{emp_id} has been changed!\n")

        elif choice == '3':
            emp_city = input("Enter the Employee's new city: ").title().strip()
            update = f"""update Employee set Employee_City = '{emp_city}' 
                            where EmployeeID = 'E{emp_id}' and Department_no = 'D{dept}'"""
            cur.execute(update)
            con.commit()
            print(f"\nCity of Employee E{emp_id} has been changed!\n")

        elif choice == '4':
            emp_phone = input("Enter the Employee's new phone number: ").strip()
            update = f"""update Employee set Phone_Number = '{emp_phone}' 
                         where EmployeeID = 'E{emp_id}' and Department_no = 'D{dept}'"""
            cur.execute(update)
            con.commit()
            print(f"\nPhone Number of Employee E{emp_id} has been changed!\n")

        elif choice == '5':
            emp_dob = input("Enter the corrected Date of birth (DD/MM/YYYY): ").strip()
            update = f"""update Employee set Date_of_birth  = '{emp_dob}' 
                         where EmployeeID = 'E{emp_id}' and Department_no = 'D{dept}'"""
            cur.execute(update)
            con.commit()
            print(f"\nPhone Number of Employee E{emp_id} has been changed!\n")

    else:
        print(f"\nThere is no employee with empID E{emp_id} in the company!\n")
