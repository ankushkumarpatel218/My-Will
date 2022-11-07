import sqlite3


con = sqlite3.connect("employee.db")


def npersonal():
    n = input("Enter Employee Name: ")
    c = input("Enter Employee's City Name:")
    d = input("Enter Employee D.O.B:")
    p = input("Enter Employee Phone:")
    sql = f"insert into personal values('{n}', '{c}', '{d}', '{p}')"
    c = con.cursor()
    c.execute(sql)
    con.commit()
    print("\nData Entered Successfully\n")
    main()


def personal():
    sql = "select * from personal"
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        print(i)
    main()


def noffice():
    ec = input("Enter Employee ID:")
    n = input("Enter Employee Name:")
    bp = int(input("Enter Assigned Salary:"))
    data = (ec, n, bp)
    sql = 'insert into office values()'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("data Entered Successfully")
    main()


def office():
    sql = "select* from office"
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        print(i)
    main()


def nsalary():
    ec = input("Enter Employee ID:")
    sql = "select Basicpay from office where Ecode=%s"
    c = con.cursor()
    c.execute(sql)
    bs = c.fetchone()
    n = input("Enter Employee Name:")
    y = input("Enter Year:")
    m = input("Enter Month:")
    wd = int(input("Enter working Days:"))
    td = int(input("Enter Total Days:"))
    fp = bs[0] / td * wd
    data = (ec, n, y, m, wd, fp)
    sql = 'insert into salary values(%s,%s,%s,%s,%S,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data Entered Successfully")
    main()


def salary():
    sql = "select*from salary"
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        print(i)
    main()


def main():
    print(""" 1.Add New Employee personal Details
 2.Display Employee personal Details
 3.Add New Employee office Details
 4.Dispaly Employee office Details
 5.Enter Salary Details of Employee
 6.Dispaly Salary Details of Employee\n""")
    choice = input("Enter Task No:")
    while True:
        if (choice == '1'):
            npersonal()
        elif choice == '2':
            personal()
        elif (choice == '3'):
            noffice()
        elif (choice == '4'):
                office()
        elif choice == '5':
            nsalary()
        elif choice == '6':
            salary()
        else:
            print("wrong choice........")
            break
main()

