import sqlite3
from prettytable import PrettyTable
con = sqlite3.connect('Library.db')
cur = con.cursor()

# Show the all Books Which are not Returned yet
def show_not_return_book():
    print("******************************************\n"
          "Show the all books which are not returned -\n"
          "******************************************")
    sql = f"""Select * from Register 
            where Status = 'Issued'"""
    cur.execute(sql)
    res = cur.fetchall()
    con.commit()
    header = ["Accession_no", "Issuer_Name", "Issuer_ID", "Book_name",
              "BookID", "Status", "Issued_Date", "Return_Date"]
    table = PrettyTable(header)
    for i in res:
        data = list(i)
        table.add_row(data)
    print(table)
