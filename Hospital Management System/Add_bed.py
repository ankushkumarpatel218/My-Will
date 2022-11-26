import sqlite3
con = sqlite3.connect('Hospital Management System.db')
cur = con.cursor()

def add_bed():
    print("********************\n"
          "Add Bed in the Ward -\n"
          "********************")
    global Room_type
    print("***************************************************\n"
          "Ward Number = Floor no. + No. of beds in that floor\n"
          "Example - 01013 -> Floor = 01 and no of beds = 013\n"
          "*************************************************")
    ward_number = input("Enter the Ward number ( 5-digit ): ").strip()
    bed_number = input("Enter the Bed number ( 2-digits ): ").strip()
    print("""1.Sweat Room
2.Private
3.Twin Sharing Room
4.General Ward
5.Isolation Room""")
    choice = input("Enter the Room type:")
    if choice == '1':
        Room_type = "Sweat Room"
    elif choice == '2':
        Room_type = "Private Room"
    elif choice == '3':
        Room_type = "Twin Sharing"
    elif choice == "4":
        Room_type = "General Ward"
    elif choice == '5':
        Room_type = 'Isolation Room'
    sql1 = f"""Select * from Hospital
                where Ward_Number = '{ward_number}' and Bed_Number = '{bed_number}'"""
    cur.execute(sql1)
    res = cur.fetchall()
    if len(res) == 0:
        sql = f"""insert into Hospital
                values('{ward_number}','{bed_number}','{Room_type}','Available')"""
        cur.execute(sql)
        con.commit()
        print("\nBed Has Been Added!")
    else:
        print(f"\nBed {bed_number} is already in Ward {ward_number}\n")
