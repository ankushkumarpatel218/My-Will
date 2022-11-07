import sqlite3
con = sqlite3.connect('Library.db')
cur = con.cursor()


def add_book():
    qry1 = input('enter Accession Number: ')
    qry2 = input('enter Book name:')
    qry3 = input('enter Book ID:')
    author = input("Enter the Author of the book: ")
    qry4 = input('enter Publisher_name')
    qry5 = input('enter pubID')
    sql = f'''insert into library(Accession_no, Book_Name, BookId, Pub_Name, PubID, Status)
                    values("{qry1}","{qry2}","{qry3}","{author}","{qry4}", "{qry5}", 'Available')'''
    cur.execute(sql)
    con.commit()
    print("\n Data Entered Successfully!\n")
