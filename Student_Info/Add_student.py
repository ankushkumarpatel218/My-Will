import sqlite3
con = sqlite3.connect("Student.db")
cur = con.cursor()


def add_stu():
    global Class
    print("***********************\n"
          "Enter New Student Data:\n"
          "***********************")
    admi = input("Enter Admission number ( 4-Digits ): ").strip()
    name = input("Enter Student Name:").title().strip()
    print("""*****************
1. Class 1st
2. Class 2nd
3. Class 3rd
4. Class 4th
5. Class 5th
6. Class 6th
7. Class 7th
8. Class 8th
9. Class 9th
10. Class 10th
11. Class 11th
12. Class 12th\n*****************""")
    choice1 = input("Enter Class of the student: ").strip()
    if choice1 == '1':
        print("""**************
A. Section-A
B. Section-B\n**************""")
        choice = input("Enter the Section of the Class: ").upper()
        if choice == "A":
            Class = "1-A"
        elif choice == 'B':
            Class = "1-B"
    elif choice1 == '2':
        print("""**************
A. Section-A
B. Section-B\n**************""")
        choice = input("Enter the Section of the Class: ").upper()
        if choice == "A":
            Class = "2-A"
        elif choice == 'B':
            Class = "2-B"
    elif choice1 == '3':
        print("""**************
A. Section-A
B. Section-B\n**************""")
        choice = input("Enter the Section of the Class: ").upper()
        if choice == "A":
            Class = "3-A"
        elif choice == 'B':
            Class = "3-B"
    elif choice1 == '4':
        print("""**************
A. Section-A
B. Section-B\n**************""")
        choice = input("Enter the Section of the Class: ").upper()
        if choice == "A":
            Class = "4-A"
        elif choice == 'B':
            Class = "4-B"
    elif choice1 == '5':
        print("""**************
A. Section-A
B. Section-B\n**************""")
        choice = input("Enter the Section of the Class: ").upper()
        if choice == "A":
            Class = "5-A"
        elif choice == 'B':
            Class = "5-B"
    elif choice1 == '6':
        print("""**************
A. Section-A
B. Section-B\n**************""")
        choice = input("Enter the Section of the Class: ").upper()
        if choice == "A":
            Class = "6-A"
        elif choice == 'B':
            Class = "6-B"
    elif choice1 == '7':
        print("""**************
A. Section-A
B. Section-B\n**************""")
        choice = input("Enter the Section of the Class: ").upper()
        if choice == "A":
            Class = "7-A"
        elif choice == 'B':
            Class = "7-B"
    elif choice1 == '8':
        print("""**************
A. Section-A
B. Section-B\n**************""")
        choice = input("Enter the Section of the Class: ").upper()
        if choice == "A":
            Class = "8-A"
        elif choice == 'B':
            Class = "8-B"
    elif choice1 == '9':
        print("""**************
A. Section-A
B. Section-B\n**************""")
        choice = input("Enter the Section of the Class: ").upper()
        if choice == "A":
            Class = "9-A"
        elif choice == 'B':
            Class = "9-B"
    elif choice1 == '10':
        print("""**************
A. Section-A
B. Section-B\n**************""")
        choice = input("Enter the Section of the Class: ").upper()
        if choice == "A":
            Class = "10-A"
        elif choice == 'B':
            Class = "10-B"
    elif choice1 == '11':
        print("""************
A. Science
B. Commerce
C. Arts\n************""")
        choice = input("Enter the Section of the Class: ").upper()
        if choice == "A":
            Class = "11th Science"
        elif choice == 'B':
            Class = "11th Commerce"
        elif choice == 'C':
            Class = "11th Arts"
    elif choice1 == '12':
        print("""************
A. Science
B. Commerce
C. Arts\n************""")
        choice = input("Enter the Section of the Class: ").upper()
        if choice == "A":
            Class = "12th Science"
        elif choice == 'B':
            Class = "12th Commerce"
        elif choice == 'C':
            Class = "12th Arts"
    else:
        print("\nPlease Enter Correct Class!\n")
        add_stu()
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
