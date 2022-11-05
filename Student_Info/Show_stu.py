import sqlite3
con = sqlite3.connect("Student.db")


def show_stu():
    user = int(input("Enter student's Admission number: "))
    print(" ")
    c = con.cursor()
    c.execute(f"select * from Student_info where admission_no = {str(user)}")
    stu_data = c.fetchall()
    for data in stu_data:
        print(data)
