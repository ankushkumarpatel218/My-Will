import sqlite3
con = sqlite3.connect('Hotel Management System.db')
cur = con.cursor()

def add_room():
    print("********************\n"
          "Add Room in the Hotel -\n"
          "********************")
    global Room_type
    floor = input("Enter the Floor number ( 2-digits ): ").strip()
    Room_number = input("Enter the Room number ( 3-digit ): ").strip()
    print("""    1.Deluxe Room
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
    sql1 = f"""Select * from Hotel 
                where Room_number = '{Room_number}' and Floor = 'F{floor}'"""
    cur.execute(sql1)
    res = cur.fetchall()
    if len(res) == 0:
        sql = f"""insert into Hotel
                values('F{floor}','{Room_number}','{Room_type}','Available')"""
        cur.execute(sql)
        con.commit()
        print("\nRoom Has Been Added!")
    else:
        print(f"\nRoom {Room_number} is already in F{floor}\n")
