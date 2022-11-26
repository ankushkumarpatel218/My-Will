import sqlite3
con = sqlite3.connect('Hospital Management System.db')
cur = con.cursor()


def remove_bed():
    print("**************************\n"
          "Remove Bed from a Ward -\n"
          "**************************")
    print("***************************************************\n"
          "Ward Number = Floor no. + No. of beds in that floor\n"
          "Example - 01013 -> Floor = 01 and no of beds = 013\n"
          "*************************************************")
    ward_number = input("Enter the Ward number ( 5-digit ): ").strip()
    bed_number = input("Enter the Bed number ( 2-digits ): ").strip()
    sql1 = f"""Select * from Hospital
                where Ward_Number = '{ward_number}' and Bed_Number = '{bed_number}'"""
    cur.execute(sql1)
    res = cur.fetchall()
    if len(res) == 1:
        sql = f"""delete from Hospital
                where Ward_Number = '{ward_number}' and Bed_Number = '{bed_number}'"""
        cur.execute(sql)
        con.commit()
        print(f"\nBed {bed_number} Has Been Removed!\n")
    else:
        print(f"\nBed {bed_number} is not in Ward {ward_number}\n")
