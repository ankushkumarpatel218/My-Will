import sqlite3
from prettytable import PrettyTable
con = sqlite3.connect('Library.db')
cur = con.cursor()

#
def search_book():
    book_name = input("Enter Book Name: ").title().strip()
    sql = f"""select * from Library 
            where Book_name = '{book_name}' and Status = 'Available'"""
    cur.execute(sql)
    res = cur.fetchall()
    num_data = len(res)
    header = ["Book_name", "BookID", "Author", "Publisher_Name", "PubID", "Status"]
    table = PrettyTable(header)
    for i in res:
        data = list(i)
        table.add_row(data)
    print(f"\nNumber of '{book_name}' in the library: {num_data}")
    print(table)