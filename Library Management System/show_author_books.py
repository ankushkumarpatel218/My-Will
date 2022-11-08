import sqlite3
from prettytable import PrettyTable
con = sqlite3.connect('Library.db')
cur = con.cursor()


# Show the all books of Particular Author
def show_aut_books():
    print("*****************************************\n"
          "Show the all books of Particular Author -\n"
          "*****************************************")
    author_name = input("Enter the Author Name: ").title().strip()
    sql = f"""Select * from library 
                where author = '{author_name}'"""
    cur.execute(sql)
    res = cur.fetchall()
    con.commit()
    header = ["Book_name", "BookID", "Author", "Publisher_Name"]
    table = PrettyTable(header)
    for i in res:
        data = list(i)
        data.pop(0)
        data.pop(-1)
        data.pop(-1)
        table.add_row(data)
    print(table)
