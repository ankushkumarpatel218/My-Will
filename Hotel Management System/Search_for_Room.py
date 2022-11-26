import sqlite3
from prettytable import PrettyTable
con = sqlite3.connect('Hotel Management System.db')
cur = con.cursor()


def search_room():
    print("************************\n"
          "Search For Particular Room -\n"
          "************************")
    floor = input("Enter the Floor number ( 2-digits ): ").strip()
    Room_number = input("Enter the Room number ( 3-digit ): ").strip()
    sql = f"""Select * from Hotel 
            where Room_number = '{Room_number}' and Floor = 'F{floor}'"""
    cur.execute(sql)
    res = cur.fetchall()
    if len(res) == 1:
        header = ["Floor", "Room_number","Room_Type","Status"]
        table = PrettyTable(header)
        for i in res:
            data = list(i)
            table.add_row(data)
        print(table)
    else:
        print("\nThere is no such room in the hotel!\n")
