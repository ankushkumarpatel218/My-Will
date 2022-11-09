import sqlite3
from prettytable import PrettyTable
con = sqlite3.connect("Student.db")


def show_num_male_female_stu():
    cur = con.cursor()
    Class = input("Enter the Class: ").lower()
    sql = f"select * from Student_info where class = '{Class}' and gender = 'Male'"
    cur.execute(sql)
    con.commit()
    res = cur.fetchall()
    M = len(res)

    sql1 = f"select * from Student_info where class = '{Class}' and gender = 'Female'"
    cur.execute(sql1)
    con.commit()
    res1 = cur.fetchall()
    F = len(res1)
    cur.execute(f"select * from Student_info where class = '{Class}'")
    con.commit()
    res = cur.fetchall()
    header = ["admission_no","Student_Name","Class", "Father_Name",
              "Mother_Name", "Date_of_Birth","Admission_Date","Phone_Number","Aadhar_Card_Number", "Gender"]
    table = PrettyTable(header)
    for i in res:
        data = list(i)
        table.add_row(data)
    print(f"\nThe number of Male in Class {Class} = {M}")
    print(f"The number of female in Class {Class} = {F}")
    print(table)

