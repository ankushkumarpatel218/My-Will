import sqlite3
con = sqlite3.connect('Library.db')
cur = con.cursor()


def add_book():
    print("*********************\n"
          "Enter New Book Data:\n"
          "*********************")
    book_id = input('Enter Book ID ( 4-digit ):').strip()
    book_name = input('Enter Book name:').title().strip()
    sql = f"select * from Library where BookID = '{book_id}'"
    cur.execute(sql)
    res = cur.fetchall()
    len1 = len(res)
    if len1 == 1:
        print(f"\nThis book data is already in the table! ")
    else:
        author = input("Enter the Author of the book: ").title().strip()
        pub_name = input('Enter Publisher_name: ').title().strip()
        pub_id = input('Enter pubID ( 6-digit ): ').strip()
        sql = f'''insert into library
                    values("{book_name}","{book_id}","{author}","{pub_name}", "{pub_id}", 'Available')'''
        cur.execute(sql)
        con.commit()
        print("\n Data Entered Successfully!\n")

    if input("Wanna Stop Entering Data?") == '*':
        pass
    else:
        add_book()
