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
    acc_no = 1001 + num_data
    issuer_id = input("Enter the Issuer Id ( 5-digit ): ").strip()
    issuer_name = input("Enter the Issuer's Name: ").title().strip()
    now = datetime.datetime.now()
    status = 'Issued'
    return1 = 'None'
    issued_date = now.strftime(f"%d/%m/{20}%y")
    book_id = input('Enter Book ID ( 4-digit ):').strip()
    sql = f"""select * from Library where BookID = '{book_id}'"""
    cur.execute(sql)
    con.commit()
    data = cur.fetchone()
    try:
        book_name = data[0]
    except Exception:
        print("\nWrong Book ID!\n")
    if data[5] == "Available":

        insert = f"""insert into Register 
                    values('{acc_no}', '{issuer_name}', '{issuer_id}', '{book_name}',
                     '{book_id}', '{status}', '{issued_date}', '{return1}')"""
        cur.execute(insert)
        update = f"""update Library set Status = 'Issued'
                    where BookID = '{book_id}'"""
        cur.execute(update)
        con.commit()
        print("\nThe Book Issued Successfully!\n")

    else:
        print("\nThis Book is already Issued by someone!")
