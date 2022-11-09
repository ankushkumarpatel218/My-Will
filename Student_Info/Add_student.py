import sqlite3
con = sqlite3.connect("Student.db")
cur = con.cursor()

def add_stu():
    admi = input("Enter Admission number ( 4-Digits ): ").strip()
    name = input("Enter Student Name:").title().strip()
    Class = input("Enter Class of the student: ").lower().strip()
    F_name = input("Enter the Father's name: ").title().strip()
    M_name = input("Enter the Mother's name: ").title().strip()
    dob = input("Enter the Student's Date of birth ( DD/MM/YYYY ):").strip()
    admission_date = input("Enter the Student's Admission Date( DD/MM/YYYY ):").strip()
    aadhar = input("Enter the Aadhar Card number of the Student (XXXX XXXX XXXX): ")
    phno = input("Enter Student's Phone number: ").strip()
    gender = input("Enter the student Gender: ").title().strip()

    Insert = f"insert into Student_info values('{admi}', '{name}', '{Class}', '{F_name}','" \
             f"{M_name}', '{dob}','{admission_date}','{phno}','{aadhar}','{gender}')"
    cur.execute(Insert)
    con.commit()
    print("\nData Entered Successfully\n")