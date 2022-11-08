import sqlite3
con = sqlite3.connect('Library.db')
cur = con.cursor()


def add_book():
    print("*********************\n"
          "Enter New Book Data:\n"
          "*********************")
    acc_no = input('Enter Accession Number ( 4-digit ): ').strip()
    Book_name = input('Enter Book name:').title().strip()
    book_id= input('Enter Book ID ( 4-digit ):').strip()
    sql = f"select * from Library where BookID = '{book_id}'"
    cur.execute(sql)
    res = cur.fetchall()
    Len1 = len(res)
    if Len1 == 1:
        print(f"\nThis book data is already in the table! ")
    else:
        author = input("Enter the Author of the book: ").title().strip()
        Pub_name = input('Enter Publisher_name: ').title().strip()
        PubID = input('Enter pubID ( 6-digit ): ').strip()
        sql = f'''insert into library
                    values("{acc_no}","{Book_name}","{book_id}","{author}","{Pub_name}", "{PubID}", 'Available')'''
        cur.execute(sql)
        con.commit()
        print("\n Data Entered Successfully!\n")

    if input("Wanna Stop Entering Data?") == '*':
        pass
    else:
        add_book()