import sqlite3
con = sqlite3.connect('Library.db')
cur = con.cursor()


def add_book():
    print("*********************\n"
          "Enter New Book Data:\n"
          "*********************")
    qry1 = input('Enter Accession Number ( 4-digit ): ')
    qry2 = input('Enter Book name:').title()
    book_id= input('Enter Book ID ( 4-digit ):')
    sql = f"select * from Library where BookID = '{book_id}'"
    cur.execute(sql)
    res = cur.fetchall()
    Len1 = len(res)
    if Len1 == 1:
        print(f"\nThis book data is already in the table! ")
    else:
        author = input("Enter the Author of the book: ")
        qry4 = input('Enter Publisher_name: ').title()
        qry5 = input('Enter pubID ( 6-digit ): ')
        sql = f'''insert into library(Accession_no, Book_Name, BookID, Pub_Name, PubID, Status)
                    values("{qry1}","{qry2}","{book_id}","{author}","{qry4}", "{qry5}", 'Available')'''
        cur.execute(sql)
        con.commit()
        print("\n Data Entered Successfully!\n")

    if input("Wanna Stop Entering Data?") == '*':
        pass
    else:
        add_book()