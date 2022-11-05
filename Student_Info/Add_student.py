import sqlite3
con = sqlite3.connect("Student.db")


def add_stu():
    admi = input("Enter Admission number: ")
    name = input("Enter Student Name:")
    Class = input("Enter Class of the student: ").lower()
    F_name = input("Enter the Father's name: ")
    M_name = input("Enter the Mother's name: ")
    dob = input("Enter Employee D.O.B:")
    phno = input("Enter Student's Phone number: ")
    gender = input("Enter student Gender: ").title()

    Insert = f"insert into Student_info values('{admi}', '{name}', '{Class}', '{F_name}','{M_name}', '{dob}', '{phno}','{gender}')"
    c = con.cursor()
    c.execute(Insert)
    con.commit()
    print("\nData Entered Successfully\n")