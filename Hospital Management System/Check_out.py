import sqlite3
import datetime
con = sqlite3.connect('Hotel Management System.db')
cur = con.cursor()


def check_out():
    floor = input("Enter the Floor number ( 2-digits ): ").strip()
    Room_number = input("Enter the Room number ( 3-digit ): ").strip()
    payment = float(input("Enter the Bill Amount: ₹"))
    now = datetime.datetime.now()
    check_out_date = now.strftime(f"%d/%m/{20}%y %H:%M:%S")
    check = f"""select Status from Hotel
                where Room_number = '{Room_number}' and Floor = 'F{floor}'"""
    cur.execute(check)
    res = cur.fetchone()
    if res[0] == 'Occupied':
        sql = f"""update Hotel_Register
                set Check_Out_Date = '{check_out_date}', Payment = '₹{payment}'
                where Room_number = '{Room_number}' and Floor = 'F{floor}'"""
        cur.execute(sql)
        sql1 = f"""update Hotel
                    set Status = 'Available'
                    where Floor = 'F{floor}' and Room_number = '{Room_number}'"""
        cur.execute(sql1)
        con.commit()
        print("\nRoom Checked Out!\n")
    else:
        print("\nThis Room is not Occupied by someone!\n")