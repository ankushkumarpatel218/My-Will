import sqlite3
import datetime

con = sqlite3.connect('Library.db')
cur = con.cursor()


def issue_book():
    issuerID = input("Enter the Issuer Id: ")
    issuerName = input("Enter the Issuer's Name: ")
    now = datetime.datetime.now()
    issued_date = now.strftime(f"%d/%m/{20}%y")
    bookid = input('Enter Book Id number: ')
    sql = f"""insert into """
    cur.execute(sql)
    con.commit()
    print("\nThe Book Issued Successfully!\n")





