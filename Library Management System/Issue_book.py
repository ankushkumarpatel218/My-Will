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
    try:
        num_data = len(res)
    except Exception:
        num_data = 0
    acc_no = 1001 + num_data
    while True:
        issuer_id = input("Enter the Issuer Id ( 5-digit ): ").strip()
        if len(issuer_id) == 5:
            pass
        else:
            print("\nInvalid Issuer Id!\nPls try Again!\n")
            input("Press any key to continue...")
            continue
    while True:
        issuer_name = input("Enter the Issuer's Name: ").title().strip()
        if len(issuer_name) == 0:
            print("\nInvalid Issuer Name!\nPls try Again!\n")
            input("Press any key to continue...")
            continue
        else:
            pass

    now = datetime.datetime.now()
    status = 'Issued'
    return1 = 'None'
    issued_date = now.strftime(f"%d/%m/{20}%y")
    while True:
        book_id = input('Enter Book ID ( 4-digit ):').strip()
        sql = f"""select * from Library where BookID = '{book_id}'"""
        cur.execute(sql)
        con.commit()
        data = cur.fetchone()
        try:
            book_name = data[0]
        except Exception:
            print("\nWrong Book ID!\nPls try Again!")
            input("Press any key to continue...")
            continue
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
