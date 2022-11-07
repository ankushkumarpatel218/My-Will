import sqlite3
con = sqlite3.connect("Student.db")


def add_stu():
    admi = input("Enter Admission number: ")
    name = input("Enter Student Name:").title()
    Class = input("Enter Class of the student: ").lower()
    F_name = input("Enter the Father's name: ").title()
    M_name = input("Enter the Mother's name: ").title()
    dob = input("Enter the Student's Date of birth:")
    phno = input("Enter Student's Phone number: ")
    gender = input("Enter the student Gender: ").title()

    Insert = f"insert into Student_info values('{admi}', '{name}', '{Class}', '{F_name}','{M_name}', '{dob}', '{phno}','{gender}')"
    c = con.cursor()
    c.execute(Insert)
    con.commit()
    print("\nData Entered Successfully\n")