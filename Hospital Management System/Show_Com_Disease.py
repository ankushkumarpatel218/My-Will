import sqlite3
from prettytable import PrettyTable
con = sqlite3.connect('Hospital Management System.db')
cur = con.cursor()


def show_com_disease():
    print("*************************************\n"
          "Show the Patient With Common Disease -\n"
          "*************************************")
    disease = input("Enter the name of the disease: ").strip().title()

    sql1 = f"""Select Ward_Number,Bed_Number,Patient_Name,Disease,Hospitalization_Date
                from Hospital_Register
                where Disease = '{disease}'"""
    cur.execute(sql1)
    res = cur.fetchall()
    if len(res) > 0:
        for data in res:
            sql2 = f"""select Status from Hospital
                        where Ward_Number = '{data[0]}' and Bed_Number = '{data[1]}'"""
            cur.execute(sql2)
            con.commit()
            res1 = cur.fetchone()
            if res1[-1] == 'Occupied':
                header = ['Ward_Number', 'Bed_Number', 'Patient_Name',
                          'Disease', 'Hospitalization_Date']
                table = PrettyTable(header)
                data = list(data)
                table.add_row(data)
                print(table)