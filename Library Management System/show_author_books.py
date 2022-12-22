import sqlite3
from prettytable import PrettyTable
con = sqlite3.connect('Library.db')
cur = con.cursor()


# Show the all books of Particular Author
def show_aut_books():
    print("*****************************************\n"
          "Show the all books of Particular Author -\n"
          "*****************************************")
    Condition = True
    while Condition:
        author = input("Enter the Author of the book: ").strip().title()
        if len(author) == 0:
            print("\nAuthor must be at least 1 character\nPls Try Again!\n")
            continue
        else:
            Condition = False
    sql = f"""Select * from library 
                where author = '{author}'"""
    cur.execute(sql)
    res = cur.fetchall()
    con.commit()
    header = ["Book_name", "BookID", "Author", "Publisher_Name"]
    table = PrettyTable(header)
    for i in res:
        data = list(i)
        data.pop(-1)
        data.pop(-1)
        table.add_row(data)
    print(table)
