import sqlite3
import datetime
con = sqlite3.connect('Hospital Management System.db')
cur = con.cursor()


def discharge():
    print("********************\n"
          "Discharge a Patient -\n"
          "********************")
    print("***************************************************\n"
          "Ward Number = Floor no. + No. of beds in that floor\n"
          "Example - 01013 -> Floor = 01 and no of beds = 013\n"
          "*************************************************")
    now = datetime.datetime.now()
    discharge_date = now.strftime(f"%d/%m/{20}%y %H:%M:%S")
    ward_number = input("Enter the Ward number ( 5-digit ): ").strip()
    bed_number = input("Enter the Bed number ( 2-digits ): ").strip()

    sql1 = f"""Select Status,Room_Type from Hospital
                where Ward_Number = '{ward_number}' and Bed_Number = '{bed_number}'"""
    cur.execute(sql1)
    res = cur.fetchone()
    if res[0] == 'Occupied':
        payment = float(input("Enter the Bill Amount: ₹"))
        sql = f"""update Hospital_Register
                set Discharging_Date = '{discharge_date}', Payment = '₹{payment}'
                where Ward_Number = '{ward_number}' and Bed_Number = '{bed_number}'"""
        cur.execute(sql)
        sql1 = f"""update Hospital
                    set Status = 'Available'
                    where Ward_Number = '{ward_number}' and Bed_Number = '{bed_number}'"""
        cur.execute(sql1)
        con.commit()
        print("\nPatient Has Been Discharged!\n")
    else:
        print(f"\nThere is no patient in bed {bed_number}, ward {ward_number}!\n")