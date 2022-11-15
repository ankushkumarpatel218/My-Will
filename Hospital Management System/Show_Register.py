import sqlite3
from prettytable import PrettyTable
con = sqlite3.connect('Hotel Management System.db')
cur = con.cursor()


def show_register():
    print("***************************\n"
          "Show Register Data of Hotel -\n"
          "***************************")
    sql = f"Select * from Hotel_Register"
    cur.execute(sql)
    res = cur.fetchall()
    header = ["Floor", "Room_number", "Guest_Name", "Payment", "No._of_Days", "No. of_Night",
             "Check_In_Date", "Check_Out_Date"]
    table = PrettyTable(header)
    for i in res:
        data = list(i)
        table.add_row(data)
    print(table)
