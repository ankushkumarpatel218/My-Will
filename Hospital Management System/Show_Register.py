import sqlite3
from prettytable import PrettyTable
con = sqlite3.connect('Hospital Management System.db')
cur = con.cursor()


def show_register():
    print("*********************\n"
          "Show Patient Register -\n"
          "*********************")
    sql = f"Select * from Hospital_Register"
    cur.execute(sql)
    res = cur.fetchall()
    header = ['Ward_Number', 'Bed_Number', 'Room_Type', 'Patient_Name',
              'Disease', 'Payment','Hospitalization_Date', 'Discharging_Date']
    table = PrettyTable(header)
    for i in res:
        data = list(i)
        table.add_row(data)
    print(table)
