import sqlite3
import datetime
con = sqlite3.connect('Library.db')
cur = con.cursor()


def return_book():
    print("************************\n"
          "Entry of Returning Book-\n"
          "************************")
    book_id = input('Enter Book ID ( 4-digit ):').strip()
    now = datetime.datetime.now()
    return_date = now.strftime(f"%d/%m/{20}%y")
    sql = f"select * from Library where BookID = '{book_id}'"
    cur.execute(sql)
    res = cur.fetchone()
    status = 'Issued'
    if res[5] == status:
        issuer_id = input("Enter Issuer ID ( 5-Digit ): ").strip()
        Return = f"""Update Register set Status = 'Returned', Return_Date = '{return_date}' 
                        where BookID = '{book_id}' and Issuer_ID = '{issuer_id}'"""
        cur.execute(Return)

        Return1 = f"""Update Library set Status = 'Available'
                        where BookID = '{book_id}'"""
        cur.execute(Return1)
        con.commit()
        print("\nThe Book Returned Successfully!")
    else:
        print("\nThis Book hasn't been Issued yet!")
