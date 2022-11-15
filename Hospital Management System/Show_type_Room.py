import sqlite3
from prettytable import PrettyTable
con = sqlite3.connect('Hotel Management System.db')
cur = con.cursor()


def search_type_room():
    print("********************************\n"
          "Show the Particular Type of Room -\n"
          "********************************")
    global Room_type
    print("""    1.Delux Room
    2.Couple Room
    3.Family Room
    4.Normal Room""")
    choice = input("Enter the Room type:")
    if choice == '1':
        Room_type = "Deluxe"
    elif choice == '2':
        Room_type = "Couple"
    elif choice == '3':
        Room_type = "Family"
    elif choice == "4":
        Room_type = "Normal"
    sql = f"""Select * from Hotel 
            where Status = 'Available' and Room_Type = '{Room_type}'"""
    cur.execute(sql)
    res = cur.fetchall()
    header = ["Floor", "Room_number","Room_Type","Status"]
    table = PrettyTable(header)
    for i in res:
        data = list(i)
        table.add_row(data)
    print(table)
