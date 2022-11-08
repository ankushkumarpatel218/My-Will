import sqlite3
con = sqlite3.connect("Student.db")


def update_stu():
    cur = con.cursor()
    admi = input("Enter Admission number: ")
    print("""1.admission_no
    2.Student_Name
    3.Class
    4.Father_Name
    5.Mother_Name
    6.Date_of_Birth
    7.Phone_Number
    8.Gender\n""")
    info = input('Which data you want to update? ')
    if info == '1':
        new_data = input('enter the new Admission number: ')
        sql = f"""update Student_info
                set Admission_no ='{new_data}'
                where admission_no = '{admi}'"""
        cur.execute(sql)
        con.commit()
        print(f'\nData Updated Successfully!\n')

    elif info == '2':
        new_data = input('enter the new name: ')
        sql = f"""update Student_info
                        set Student_Name ='{new_data}'
                        where admission_no = '{admi}'"""
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        print(f'\nData Updated Successfully!\n')

    elif info == '3':
        new_data = input('enter the updated class: ').lower()
        sql = f"""update Student_info
                set Class ='{new_data}'
                where admission_no = '{admi}'"""
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        print(f'\nData Updated Successfully!\n')

    elif info == '4':
        new_data = input('enter the updated father name: ')
        sql = f"""update Student_info
                    set Father_Name ='{new_data}'
                    where admission_no = '{admi}'"""
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        print(f'\nData Updated Successfully!\n')

    elif info == '5':
        new_data = input('enter the updated mother name: ')
        sql = f"""update Student_info
                set Mother_Name ='{new_data}'
                where admission_no = '{admi}'"""
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        print(f'\nData Updated Successfully!\n')

    elif info == '6':
        new_data = input('enter the updated DOB: ')
        sql = f"""update Student_info
                set Date_of_Birth ='{new_data}'
                where admission_no = '{admi}'"""
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        print(f'\nData Updated Successfully!\n')

    elif info == '7':
        new_data = input('enter the new Phone number: ')
        sql = f"""update Student_info
                set Phone_Number ='{new_data}'
                where admission_no = '{admi}'"""
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        print(f'\nData Updated Successfully!\n')

    elif info == '8':
        new_data = input('enter the correct gender of the student: ').title()
        sql = f"""update Student_info
                set Gender ='{new_data}'
                where admission_no = '{admi}'"""
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        print(f'\nData Updated Successfully!\n')