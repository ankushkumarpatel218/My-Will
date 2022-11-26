import sqlite3
from prettytable import PrettyTable
con = sqlite3.connect('Hospital Management System.db')
cur = con.cursor()


def search_type_room():
    print("********************************\n"
          "Show the Particular Type of Room -\n"
          "********************************")
    global Room_type
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
                    where Room_Type = '{Room_type}'"""
    cur.execute(sql1)
    res = cur.fetchall()
    if len(res) > 0 :
        header = ['Ward_Number', 'Bed_Number', 'Room_Type', 'Status']
        table = PrettyTable(header)
        for i in res:
            data = list(i)
            table.add_row(data)
        print(table)
    else:
        print("\nThere is no Such Room!\n")
