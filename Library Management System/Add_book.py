import sqlite3
con = sqlite3.connect('Library.db')
cur = con.cursor()

def add_book():
        qry1 = input('enter acc no. ')
        qry2 = input('enter Book name:')
        qry3 = input('enter Book ID:')
        qry4 = input('enter Publisher_name')
        qry5 = input('enter pubID')
        cur.execute(f'''insert into library(acc_no, book_name, bookId
                    values("{qry1}","{qry2}","{qry3}", "{qry4}", "{qry5}")''')
        con.commit()

con.close()

