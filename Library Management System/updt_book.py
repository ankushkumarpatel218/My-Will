import sqlite3
con = sqlite3.connect('Library.db')
cur = con.cursor()


def update_book():
    print("*******************\n"
          "Updating Book Data-\n"
          "*******************")
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
    res = cur.fetchall()
    len1 = len(res)
    if len1 == 1:
        print("""    1.Publisher ID
        2.Book name
        3.BookID
        4.Author
        5.Publisher Name""")

        choice = input("Enter Which Data You Want to Update: ").strip()

        if choice == '1':
            Condition = True
            while Condition:
                try:
                    pub_id = input('Enter pubID ( 6-digit ): ').strip()
                    if len(pub_id) == 6:
                        int(pub_id)
                        Condition = False
                    else:
                        print("\nPublisher ID must be 6 digits\nPls Try Again!\n")
                        continue
                except Exception as e:
                    print("\nThe Publisher ID must be Number!\n")
                    continue
            sql = f"""update Library set
                        PubID = '{pub_id}'
                        where BookID = '{book_id}'"""
            cur.execute(sql)
            con.commit()
            print("\nData Updated Successfully!")

        elif choice == '2':
            Condition = True
            while Condition:
                book_name = input('Enter Book name:').title().strip()
                if len(book_name) == 0:
                    print("\nBook Name must be at least 1 character\nPls Try Again!\n")
                    continue
                else:
                    Condition = False
            sql = f"""update Library set Book_name = '{book_name}'
                      where BookID = '{book_id}'"""
            cur.execute(sql)
            con.commit()
            print("\nData Updated Successfully!")

        elif choice == '3':
            Condition = True
            while Condition:
                try:
                    New_book_Id = input('Enter Book ID ( 4-digit ):').strip()
                    if len(book_id) == 4:
                        int(book_id)
                        Condition = False
                    else:
                        print("\nBook ID must be 4 digits\nPls Try Again!\n")
                        continue
                except Exception as e:
                    print("\nThe Book ID must be Number!\n")
                    continue
            sql = f"""update Library set BookID = '{New_book_Id}'
                      where BookID = '{book_id}'"""
            cur.execute(sql)
            con.commit()
            print("\nData Updated Successfully!")


        elif choice == '4':
            Condition = True
            while Condition:
                author = input("Enter the Author of the book: ").strip().title()
                if len(author) == 0:
                    print("\nAuthor must be at least 1 character\nPls Try Again!\n")
                    continue
                else:
                    Condition = False
            sql = f"""update Library set Author= '{author}' where BookID = '{book_id}'"""
            cur.execute(sql)
            con.commit()
            print("\nData Updated Successfully!\n")

        elif choice == '5':
            Condition = True
            while Condition:
                pub_name = input('Enter Publisher_name: ').title().strip()
                if len(pub_name) == 0:
                    print("\nPublisher_name must be at least 1 character\nPls Try Again!\n")
                    continue

                else:
                    Condition = False
            sql = f"""update Library set Pub_Name = '{pub_name}' 
                      where BookID = '{book_id}'"""
            cur.execute(sql)
            con.commit()
            print("\nData Updated Successfully!\n")


        else:
            print(f"\nThe choice is incorrect!\n")
            update_book()
    else:
        print(f"\nBook With {book_id} this ID is not in the Library!\n")