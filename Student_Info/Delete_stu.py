import sqlite3
con = sqlite3.connect("Student.db")
cur = con.cursor()

def del_stu():
    print("********************\n"
          "Delete Student Data:\n"
          "********************")
    admi = input("Enter Admission number of the student: ")
    sql = f"delete from Student_info where admission_no = '{admi}'"
    cur.execute(sql)
    con.commit()
    print('\n The Data Successfully Deleted!\n')
