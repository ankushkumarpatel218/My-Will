import sqlite3
con = sqlite3.connect('Hotel Management System.db')
cur = con.cursor()


def remove_room():
    print("**************************\n"
          "Remove Room From the Hotel -\n"
          "**************************")
    floor = input("Enter the Floor number: ").strip()
    Room_number = input("Enter the Room number: ").strip()
    sql1 = f"""Select * from Hotel 
                    where Room_number = '{Room_number}' and Floor = 'F{floor}'"""
    cur.execute(sql1)
    res = cur.fetchall()
    if len(res) == 1:
        sql = f"""delete from Hotel
                Where Room_number = '{Room_number}' and Floor = 'F{floor}'"""
        cur.execute(sql)
        con.commit()
        print("\nRoom Has Been Removed!\n")
    else:
        print(f"\nRoom {Room_number} doesn't Exist!\n")
