import sqlite3
from prettytable import PrettyTable
con = sqlite3.connect("Student.db")


def show_num_male_female_stu():
    print("*****************************************\n"
          "Show Number of Male/Female Students Data:\n"
          "*****************************************")
    global Class
    cur = con.cursor()
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
    Choice = input("Enter Class of the student: ").strip()
    if Choice == '1':
        print("""**************
A. Section-A
B. Section-B\n**************""")
        choice = input("Enter the Section of the Class: ").upper()
        if choice == "A":
            Class = "1-A"
        elif choice == 'B':
            Class = "1-B"
    elif Choice == '2':
        print("""**************
A. Section-A
B. Section-B\n**************""")
        choice = input("Enter the Section of the Class: ").upper()
        if choice == "A":
            Class = "2-A"
        elif choice == 'B':
            Class = "2-B"
    elif Choice == '3':
        print("""**************
A. Section-A
B. Section-B\n**************""")
        choice = input("Enter the Section of the Class: ").upper()
        if choice == "A":
            Class = "3-A"
        elif choice == 'B':
            Class = "3-B"
    elif Choice == '4':
        print("""**************
A. Section-A
B. Section-B\n**************""")
        choice = input("Enter the Section of the Class: ").upper()
        if choice == "A":
            Class = "4-A"
        elif choice == 'B':
            Class = "4-B"
    elif Choice == '5':
        print("""**************
A. Section-A
B. Section-B\n**************""")
        choice = input("Enter the Section of the Class: ").upper()
        if choice == "A":
            Class = "5-A"
        elif choice == 'B':
            Class = "5-B"
    elif Choice == '6':
        print("""**************
A. Section-A
B. Section-B\n**************""")
        choice = input("Enter the Section of the Class: ").upper()
        if choice == "A":
            Class = "6-A"
        elif choice == 'B':
            Class = "6-B"
    elif Choice == '7':
        print("""**************
A. Section-A
B. Section-B\n**************""")
        choice = input("Enter the Section of the Class: ").upper()
        if choice == "A":
            Class = "7-A"
        elif choice == 'B':
            Class = "7-B"
    elif Choice == '8':
        print("""**************
A. Section-A
B. Section-B\n**************""")
        choice = input("Enter the Section of the Class: ").upper()
        if choice == "A":
            Class = "8-A"
        elif choice == 'B':
            Class = "8-B"
    elif Choice == '9':
        print("""**************
A. Section-A
B. Section-B\n**************""")
        choice = input("Enter the Section of the Class: ").upper()
        if choice == "A":
            Class = "9-A"
        elif choice == 'B':
            Class = "9-B"
    elif Choice == '10':
        print("""**************
A. Section-A
B. Section-B\n**************""")
        choice = input("Enter the Section of the Class: ").upper()
        if choice == "A":
            Class = "10-A"
        elif choice == 'B':
            Class = "10-B"
    elif Choice == '11':
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
    elif Choice == '12':
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
    sql = f"select * from Student_info where class = '{Class}' and gender = 'Male'"
    cur.execute(sql)
    con.commit()
    res = cur.fetchall()
    M = len(res)

    sql1 = f"select * from Student_info where class = '{Class}' and gender = 'Female'"
    cur.execute(sql1)
    con.commit()
    res1 = cur.fetchall()
    F = len(res1)
    cur.execute(f"select * from Student_info where class = '{Class}'")
    con.commit()
    res = cur.fetchall()
    header = ["admission_no","Student_Name","Class", "Father_Name",
              "Mother_Name", "Date_of_Birth","Admission_Date","Phone_Number","Aadhar_Card_Number", "Gender"]
    table = PrettyTable(header)
    for i in res:
        data = list(i)
        table.add_row(data)
    print(f"\nThe number of Male in Class {Class} = {M}")
    print(f"The number of female in Class {Class} = {F}")
    print(table)

