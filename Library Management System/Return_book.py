import sqlite3
import datetime
con = sqlite3.connect('Library.db')
cur = con.cursor()


def return_book():
    print("************************\n"
          "Entry of Returning Book-\n"
          "************************")
    Condition = True
    while Condition:
        try:
            book_id = input('Enter Book ID ( 4-digit ):').strip()
            if len(book_id) == 4:
                int(book_id)
                Condition = False
            else:
                print("\nBook ID must be 4 digits\nPls Try Again!\n")
                continue
        except Exception as e:
            print("\nThe Book ID must be Number!\n")
            continue
    sql = f"select * from Library where BookID = '{book_id}'"
    cur.execute(sql)
    res = cur.fetchone()
    if res == None:
        print(f"\nThere is no Book with BookID {book_id} has issued!\n")
    else:
        now = datetime.datetime.now()
        return_date = now.strftime(f"%d/%m/{20}%y")
        status = 'Issued'
        if res[5] == status:
            issuer_id = input("Enter Issuer ID ( 5-Digit ): ").strip()
            Return = f"""Update Register set Status = 'Returned',
                         Return_Date = '{return_date}' 
                        where BookID = '{book_id}' and Issuer_ID = '{issuer_id}'"""
            cur.execute(Return)
            
            Return1 = f"""Update Library set Status = 'Available' 
                          where BookID = '{book_id}'"""
            
            cur.execute(Return1)
            con.commit()
            print("\nThe Book Returned Successfully!")
        else:
            print("\nThis Book hasn't been Issued yet!")