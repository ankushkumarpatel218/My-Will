import sqlite3
con = sqlite3.connect("Student.db")


def update_stu():
    print("*********************\n"
          "Update Students Data:\n"
          "*********************")
    cur = con.cursor()
    admission_number = input("Enter Admission number of the Student: ")
    print("""1.admission_no
2.Student_Name
3.Class
4.Father_Name
5.Mother_Name
6.Date_of_Birth
7.Phone_Number
8.Gender
9.Aadhar Card Number
10.Admission Date\n""")
    info = input('Which data you want to update? ')
    if info == '1':
        new_data = input('enter the corrected Admission number: ')
        sql = f"""update Student_info
                set Admission_no ='{new_data}'
                where admission_no = '{admission_number}'"""
        cur.execute(sql)
        con.commit()
        print(f'\nData Updated Successfully!\n')

    elif info == '2':
        new_data = input('enter the corrected name: ')
        sql = f"""update Student_info
                        set Student_Name ='{new_data}'
                        where admission_no = '{admission_number}'"""
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        print(f'\nData Updated Successfully!\n')

    elif info == '3':
        global Class
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
        sql = f"""update Student_info
                set Class ='{Class}'
                where admission_no = '{admission_number}'"""
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        print(f'\nData Updated Successfully!\n')

    elif info == '4':
        new_data = input('enter the corrected father name: ')
        sql = f"""update Student_info
                    set Father_Name ='{new_data}'
                    where admission_no = '{admission_number}'"""
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        print(f'\nData Updated Successfully!\n')

    elif info == '5':
        new_data = input('enter the corrected mother name: ')
        sql = f"""update Student_info
                set Mother_Name ='{new_data}'
                where admission_no = '{admission_number}'"""
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        print(f'\nData Updated Successfully!\n')

    elif info == '6':
        new_data = input('enter the corrected DOB: ')
        sql = f"""update Student_info
                set Date_of_Birth ='{new_data}'
                where admission_no = '{admission_number}'"""
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        print(f'\nData Updated Successfully!\n')

    elif info == '7':
        new_data = input('enter the new Phone number: ')
        sql = f"""update Student_info
                set Phone_Number ='{new_data}'
                where admission_no = '{admission_number}'"""
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        print(f'\nData Updated Successfully!\n')

    elif info == '8':
        new_data = input('enter the correct gender of the student: ').title()
        sql = f"""update Student_info
                set Gender ='{new_data}'
                where admission_no = '{admission_number}'"""
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        print(f'\nData Updated Successfully!\n')

    elif info == '9':
        new_data = input('enter the corrected Aadhar card Number: ').title()
        sql = f"""update Student_info
                set Gender ='{new_data}'
                where admission_no = '{admission_number}'"""
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        print(f'\nData Updated Successfully!\n')

    elif info == '10':
        new_data = input('enter the corrected Admission date: ').title()
        sql = f"""update Student_info
                set Gender ='{new_data}'
                where admission_no = '{admission_number}'"""
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        print(f'\nData Updated Successfully!\n')

    else:
        print("Wrong Option!...Pls try Again!")
        update_stu()
