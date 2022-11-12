import sqlite3
import datetime
con = sqlite3.connect('Hotel Management System.db')
cur = con.cursor()


def check_in():
    print("*************\n"
          "Check In Room -\n"
          "*************")
    floor = input("Enter the Floor number ( 2-digits ): ").strip()
    Room_number = input("Enter the Room number ( 3-digit ): ").strip()
    name = input("Enter the Name of then guest: ").title().strip()
    num_days = input("Enter Number of days the guest is Staying: ").strip()
    num_night = input("Enter Number of night the guest is Staying: ").strip()
    now = datetime.datetime.now()
    check_in_date = now.strftime(f"%d/%m/{20}%y %H:%M:%S")

    check = f"""select Status from Hotel
            where Room_number = '{Room_number}' and Floor = 'F{floor}'"""
    cur.execute(check)
    res = cur.fetchone()
    if res[0] == 'Available':
        sql = f"""insert into Hotel_Register
                values('F{floor}', '{Room_number}','{name}','-','{num_days}',
                '{num_night}','{check_in_date}','-')"""
        cur.execute(sql)
        sql1 = f"""update Hotel
                set Status = 'Occupied'
                where Floor = 'F{floor}' and Room_number = '{Room_number}'"""
        cur.execute(sql1)
        con.commit()
        print("\nRoom Has Been Register!\n")
    else:
        print("\nThis Room is Occupied by someone!\n")

