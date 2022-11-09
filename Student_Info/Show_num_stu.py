import sqlite3
from prettytable import PrettyTable
con = sqlite3.connect("Student.db")


def show_num_stu():
    cur = con.cursor()
    Class = input("Enter the Class: ").lower()
    cur.execute(f"select * from Student_info where class = '{Class}'")
    con.commit()
    res = cur.fetchall()
    total = len(res)
    header = ["admission_no", "Student_Name", "Class", "Father_Name",
              "Mother_Name", "Date_of_Birth", "Admission_Date", "Phone_Number", "Aadhar_Card_Number", "Gender"]
    table = PrettyTable(header)
    for i in res:
        data = list(i)
        table.add_row(data)
    print(f'\nThe total number of student in class {Class}: {total}')
    print(table)
