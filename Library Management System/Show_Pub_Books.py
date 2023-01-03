import sqlite3
from prettytable import PrettyTable

con = sqlite3.connect('Library.db')
cur = con.cursor()


# Show the all books published by particular publisher

def show_pub_books():
    print("************************************************\n"
          "Show all Books Publish by particular Publisher -\n"
          "************************************************")

    Condition = True
    while Condition:
        try:
            pub_id = input('Enter pubID ( 6-digit ): ').strip()
            if len(pub_id) == 6:
                int(pub_id)
                Condition = False
            else:
                print("\nPublisher ID must be 6 digits\nPls Try Again!\n")
                continue
        except Exception as e:
            print("\nThe Publisher ID must be Number!\n")
            continue
    sql = f"""Select * from Library where PubID = '{pub_id}'"""
    cur.execute(sql)
    res = cur.fetchall()
    con.commit()
    header = ["Book_name", "BookID", "Author", "Publisher_Name", "PubID"]
    table = PrettyTable(header)
    for i in res:
        data = list(i)
        data.pop(-1)
        table.add_row(data)
    print(table)