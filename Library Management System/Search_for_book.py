import sqlite3
from prettytable import PrettyTable
con = sqlite3.connect('Library.db')
cur = con.cursor()

# Search For a Particular Book
def search_book():
    Condition = True
    while Condition:
        book_name = input('Enter Book name:').title().strip()
        if len(book_name) == 0:
            print("\nBook Name must be at least 1 character\nPls Try Again!\n")
            continue
        else:
            Condition = False  
              
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