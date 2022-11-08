import sqlite3
con = sqlite3.connect('Library.db')
cur = con.cursor()


def Remove_book():
    print("*********************\n"
          "Removing a Book Data-\n"
          "*********************")
    book_id = input("Enter the book ID ( 4-Digit ): ")
    delete = f'delete from Library where BookID = "{book_id}"'
    cur.execute(delete)
    con.commit()
    print('\n The Book Data Successfully Deleted!')