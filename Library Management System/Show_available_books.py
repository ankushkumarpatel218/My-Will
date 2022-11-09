import sqlite3
from prettytable import PrettyTable

con = sqlite3.connect('Library.db')
cur = con.cursor()

#show all Available Books
def show_avl_books():
    print("*******************************\n"
          "Show all Available Books Data -\n"
          "*******************************")
    sql = f"""Select * from Library
                where Status = 'Available'"""
    cur.execute(sql)
    res = cur.fetchall()
    con.commit()
    header = ["Book_name", "BookID", "Author", "Publisher_Name", "PubID", "Status"]
    table = PrettyTable(header)
    for i in res:
        data = list(i)
        table.add_row(data)
    print(table)
