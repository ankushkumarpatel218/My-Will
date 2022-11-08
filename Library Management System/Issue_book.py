import sqlite3
import datetime

con = sqlite3.connect('Library.db')
cur = con.cursor()

def issue_book():
    print("**********************\n"
          "Entry of Issuing Book-\n"
          "**********************")
    acc_no = input('Enter the accession number( 4-digit ):')
    issuerID = input("Enter the Issuer Id ( 5-digit ): ")
    issuerName = input("Enter the Issuer's Name: ")
    now = datetime.datetime.now()
    status = 'Issued'
    Return = 'None'
    issued_date = now.strftime(f"%d/%m/{20}%y")
    book_id= input('Enter Book ID ( 4-digit ):')
    sql = f"""select * from Library where BookID = '{book_id}'"""
    cur.execute(sql)
    con.commit()
    data = cur.fetchone()
    book_name = data[1]
    if data[6] == "Available":
        insert = f"""insert into Register 
                    values('{acc_no}', '{issuerName}', '{issuerID}', '{book_name}',
                     '{book_id}', '{status}', '{issued_date}', '{Return}')"""
        cur.execute(insert)
        update = f"""update Library set Status = 'Issued'
                    where Book_ID = {book_id}"""
        cur.execute(update)
        con.commit()
        print("\nThe Book Issued Successfully!\n")

    else:
        print("\nThis Book is already Issued by someone!")
        issue_book()
