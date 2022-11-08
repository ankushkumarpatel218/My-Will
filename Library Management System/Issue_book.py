import sqlite3
import datetime

con = sqlite3.connect('Library.db')
cur = con.cursor()

def issue_book():
    print("**********************\n"
          "Entry of Issuing Book-\n"
          "**********************")
    data1 = f"select * from Register"
    cur.execute(data1)
    res = cur.fetchall()
    num_data = len(res)
    acc_no = 1000 + num_data
    issuerID = input("Enter the Issuer Id ( 5-digit ): ").strip()
    issuerName = input("Enter the Issuer's Name: ").title().strip()
    now = datetime.datetime.now()
    status = 'Issued'
    Return = 'None'
    issued_date = now.strftime(f"%d/%m/{20}%y")
    book_id= input('Enter Book ID ( 4-digit ):').strip()
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
                    where BookID = '{book_id}'"""
        cur.execute(update)
        con.commit()
        print("\nThe Book Issued Successfully!\n")

    else:
        print("\nThis Book is already Issued by someone!")
        issue_book()
