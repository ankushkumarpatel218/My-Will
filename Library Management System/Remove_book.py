import sqlite3
con = sqlite3.connect('Library.db')
cur = con.cursor()


def Remove_book():
    print("*********************\n"
          "Removing a Book Data-\n"
          "*********************")
    book_id = input("Enter the book ID ( 4-Digit ): ").strip()
    sql = f"select * from Library where BookID = '{book_id}'"
    cur.execute(sql)
    res = cur.fetchall()
    len1 = len(res)
    if len1 == 1:
        delete = f'delete from Library where BookID = "{book_id}"'
        cur.execute(delete)
        con.commit()
        print('\nThe Book Data Successfully Deleted!\n')
    else:
        print(f"\nBook With {book_id} this ID is not in the Library!\n")