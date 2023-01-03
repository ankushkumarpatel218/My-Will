import sqlite3
from prettytable import PrettyTable
con = sqlite3.connect('Library.db')
cur = con.cursor()

# Show The Library Register
def show_register():
    sql = f"Select * from Register"
    cur.execute(sql)
    res = cur.fetchall()
    header = ["Accession_no","Issuer_Name","Issuer_ID","Book_name",
              "BookID","Status","Issued_Date","Return_Date"]
    table = PrettyTable(header)
    for i in res:
        data = list(i)
        table.add_row(data)
    print(table)