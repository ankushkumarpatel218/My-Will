import sqlite3
from prettytable import PrettyTable
con = sqlite3.connect('Hospital Management System.db')
cur = con.cursor()


def search_bed():
    print("***************************\n"
          "Search For Particular Room -\n"
          "***************************")
    print("***************************************************\n"
          "Ward Number = Floor no. + No. of beds in that floor\n"
          "Example - 01013 -> Floor = 01 and no of beds = 013\n"
          "*************************************************")
    ward_number = input("Enter the Ward number ( 5-digit ): ").strip()
    bed_number = input("Enter the Bed number ( 2-digits ): ").strip()
    sql1 = f"""Select Status from Hospital
                        where Ward_Number = '{ward_number}' and Bed_Number = '{bed_number}'"""
    cur.execute(sql1)
    res = cur.fetchone()
    if res[0] == 'Occupied':
        sql1 = f"""Select Ward_Number,Bed_Number,Patient_Name,Disease,Hospitalization_Date
                from Hospital_Register
                where Ward_Number = '{ward_number}' 
                and Bed_Number = '{bed_number}'"""
        cur.execute(sql1)
        res = cur.fetchall()
        if len(res) == 1:
            header = ['Ward_Number', 'Bed_Number', 'Patient_Name',
                      'Disease', 'Hospitalization_Date']
            table = PrettyTable(header)
            for i in res:
                data = list(i)
                table.add_row(data)
            print(table)

        else:
            print("\nThis room is not Occupied by Someone!\n")

