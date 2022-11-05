import sqlite3
con = sqlite3.connect("Student.db")


def show_num_stu():
    cur = con.cursor()
    Class = input("Enter the Class: ").lower()
    cur.execute(f"select * from Student_info where class = '{Class}'")
    con.commit()
    res = cur.fetchall()
    total = len(res)
    print(f'\nThe total number of student in class {Class}: {total}')