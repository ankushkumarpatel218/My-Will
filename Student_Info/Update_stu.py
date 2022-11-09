import sqlite3
con = sqlite3.connect("Student.db")


def update_stu():
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
        new_data = input('enter the updated class: ').lower()
        sql = f"""update Student_info
                set Class ='{new_data}'
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
