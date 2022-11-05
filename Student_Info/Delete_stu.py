import sqlite3
con = sqlite3.connect("Student.db")


def del_stu():
    cur = con.cursor()
    admi = input("Enter Admission number of the student: ")
    sql = f"delete from Student_info where admission_no = '{admi}'"
    cur.execute(sql)
    con.commit()
    print('\n The Data Successfully Deleted!')
