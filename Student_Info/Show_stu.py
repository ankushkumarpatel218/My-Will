import sqlite3
from prettytable import PrettyTable
con = sqlite3.connect("Student.db")


def show_stu():
    user = int(input("Enter student's Admission number: "))
    print(" ")
    c = con.cursor()
    c.execute(f"select * from Student_info where admission_no = '{user}'")
    con.commit()
    header = ["admission_no", "Student_Name", "Class", "Father_Name",
              "Mother_Name", "Date_of_Birth", "Phone_Number", "Gender"]
    res = c.fetchall()
    table = PrettyTable(header)
    for i in res:
        table.add_row(list(i))
    print(table)
