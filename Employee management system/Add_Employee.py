import sqlite3
con = sqlite3.connect("employee.db")
cur = con.cursor()

def add_emp():
    print("******************\n"
          "Add Employee Data:\n"
          "******************")
    emp_id = input("Enter The Employee Id ( 4-Digits ): E").strip()
    sql = f"select * from Employee where EmployeeID = 'E{emp_id}'"
    cur.execute(sql)
    res = cur.fetchall()
    len1 = len(res)
    if len1 == 1:
        print(f"\nThis employee with empID E{emp_id} is already in the company!\n")

    else:
        emp_name = input("Enter the Employee Name: ").title().strip()
        dept = input("Enter the Employee Department number ( 2-Digits ): D").strip()
        role = input("Enter Role of the Employee: ").strip().title()
        emp_city = input("Enter the Employee City: ").title().strip()
        Salary = input("Enter the Employee's Starting Salary: ₹").strip()
        dob = input("Enter the Employee's date of Birth ( DD/MM/YYYY ): ").strip()
        phone_no = input("Enter the Employee's phone number: ").strip()
        gender = input("Enter the Gender of the Employee: ").strip().title()

        insert = f"""insert into Employee
                    values('D{dept}','E{emp_id}','{emp_name}','{role}','{emp_city}',
                    '₹{Salary}','{dob}','{phone_no}','{gender}')"""
        cur.execute(insert)
        con.commit()
        print("\nEmployee has been Added!\n")
        
        
        

