import sqlite3
from prettytable import PrettyTable
con = sqlite3.connect('Hospital Management System.db')
cur = con.cursor()


def show_alv_bed():
    sql = f"""Select * from Hospital
            where Status = 'Available'"""
    cur.execute(sql)
    res = cur.fetchall()
    header = ['Ward_Number', 'Bed_Number', 'Room_Type', 'Status']
    table = PrettyTable(header)
    for i in res:
        data = list(i)
        table.add_row(data)
    print(table)
