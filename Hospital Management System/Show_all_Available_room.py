import sqlite3
from prettytable import PrettyTable
con = sqlite3.connect('Hotel Management System.db')
cur = con.cursor()


def show_alv_room():
    sql = f"""Select * from Hotel 
            where Status = 'Available'"""
    cur.execute(sql)
    res = cur.fetchall()
    header = ["Floor", "Room_number","Room_Type","Status"]
    table = PrettyTable(header)
    for i in res:
        data = list(i)
        table.add_row(data)
    print(table)
