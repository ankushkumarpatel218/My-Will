import sqlite3
from prettytable import PrettyTable

con = sqlite3.connect("Student.db")


def show_all_stu():
    cur = con.cursor()
    cur.execute('SELECT * FROM Student_info')
    con.commit()
    header = ["admission_no","Student_Name","Class", "Father_Name",
              "Mother_Name", "Date_of_Birth","Phone_Number", "Gender"]
    res = cur.fetchall()
    table = PrettyTable(header)
    for i in res:
        table.add_row(list(i))
    print(table)
