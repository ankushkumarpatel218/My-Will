import sqlite3
from prettytable import PrettyTable
con = sqlite3.connect("Student.db")


def show_stu():
    print("****************************\n"
          "Show Selected Students Data:\n"
          "****************************")
    user = int(input("Enter student's Admission number: "))
    print(" ")
    c = con.cursor()
    c.execute(f"select * from Student_info where admission_no = '{user}'")
    header = ["admission_no", "Student_Name", "Class", "Father_Name",
              "Mother_Name", "Date_of_Birth","Admission_Date", "Phone_Number","Aadhar_Card_Number", "Gender"]
    res = c.fetchall()
    table = PrettyTable(header)
    for i in res:
        table.add_row(list(i))
    print(table)
