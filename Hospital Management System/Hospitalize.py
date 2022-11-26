import sqlite3
import datetime
con = sqlite3.connect('Hospital Management System.db')
cur = con.cursor()


def hospitalize():
    print("**********************\n"
          "Hospitalize a Patient -\n"
          "**********************")
    print("***************************************************\n"
          "Ward Number = Floor no. + No. of beds in that floor\n"
          "Example - 01013 -> Floor = 01 and no of beds = 013\n"
          "*************************************************")
    now = datetime.datetime.now()
    hospitalize_date = now.strftime(f"%d/%m/{20}%y %H:%M:%S")
    ward_number = input("Enter the Ward number ( 5-digit ): ").strip()
    bed_number = input("Enter the Bed number ( 2-digits ): ").strip()

    sql1 = f"""Select Status,Room_Type from Hospital
                    where Ward_Number = '{ward_number}' and Bed_Number = '{bed_number}'"""
    cur.execute(sql1)
    res = cur.fetchone()
    if res[0] == 'Available':
        patient_name = input("Enter the name of the patient: ").strip().title()
        disease = input("Enter the name of the disease: ").strip().title()
        sql = f"""insert into Hospital_Register
                values('{ward_number}', '{bed_number}','{res[1]}','{patient_name}','{disease}',
                '-','{hospitalize_date}','-')"""
        cur.execute(sql)
        sql1 = f"""update Hospital
                set Status = 'Occupied'
                where Ward_Number = '{ward_number}' and Bed_Number = '{bed_number}'"""
        cur.execute(sql1)
        con.commit()
        print("\nPatient Has Been Hospitalize!\n")
    else:
        print("\nThis Bed is Occupied by someone!\n")

