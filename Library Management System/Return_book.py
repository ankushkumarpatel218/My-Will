import sqlite3
con = sqlite3.connect('Library.db')
cur = con.cursor()


def return_book():
    print("************************\n"
          "Entry of Returning Book-\n"
          "************************")
    book_id= input('Enter Book ID ( 4-digit ):')
    sql = f"select * from Library where Book_ID = '{book_id}'"
    cur.execute(sql)
    res = cur.fetchone()
    if res[6] == "Issued":
        issuer_id = input("Enter Issuer ID ( 5-Digit ): ")
        Return = f"""Update Register set Status = 'Returned'
                        where Book_ID = '{book_id}' and Issuer_ID = {issuer_id}"""
        cur.execute(Return)

        Return1 = f"""Update Library set Status = 'Available'
                        where Book_ID = '{book_id}'"""
        cur.execute(Return1)
        con.commit()
        print("\nThe Book Returned Successfully!")
    else:
        print("\nThis Book hasn't been Issued yet!")