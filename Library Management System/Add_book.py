import sqlite3
con = sqlite3.connect('Library.db')
cur = con.cursor()



def add_book():
    print("*********************\n"
          "Enter New Book Data:\n"
          "*********************")
    while True:
        book_id = input('Enter Book ID ( 4-digit ):').strip()
        if len(book_id) == 4:
            pass
        else:
            print("\nBook ID must be 4 digits\nPls Try Again!\n")
            input("Press any key to continue...")
            continue
    while True:
        book_name = input('Enter Book name:').title().strip()
        if len(book_name) == 0:
            print("\nBook Name must be at least 1 character\nPls Try Again!\n")
            input("Press any key to continue...")
            continue
    sql = f"select * from Library where BookID = '{book_id}'"
    cur.execute(sql)
    res = cur.fetchall()
    len1 = len(res)
    if len1 == 1:
        print(f"\nThis book data is already in the table! ")
        add_book()
    else:
        while True:
            author = input("Enter the Author of the book: ")
            if len(author) == 0:
                print("\nAuthor must be at least 1 character\nPls Try Again!\n")
                input("Press any key to continue...")
                continue
            else:
                pass

        while True:
            pub_name = input('Enter Publisher_name: ').title().strip()
            if len(pub_name) == 0:
                print("\nPublisher_name must be at least 1 character\nPls Try Again!\n")
                input("Press any key to continue...")
                continue

            else:
                pass
        while True:
            pub_id = input('Enter pubID ( 6-digit ): ').strip()
            if len(pub_id) == 6:
                pass
            else:
                print("\nPublisher ID must be 6 digits\nPls Try Again!\n")
                input("Press any key to continue...")
                continue
        sql = f'''insert into library
                    values("{book_name}","{book_id}","{author}","{pub_name}", "{pub_id}", 'Available')'''
        cur.execute(sql)
        con.commit()
        print("\nData Entered Successfully!\n")
        jjdbv

