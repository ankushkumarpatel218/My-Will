import sqlite3
con = sqlite3.connect('Library.db')
cur = con.cursor()


def update_book():
    print("*******************\n"
          "Updating Book Data-\n"
          "*******************")
    book_id = input('Enter Book ID ( 4-digit ): ').strip()
    print("""    1.Publisher ID
    2.Book name
    3.BookID
    4.Author
    5.Publisher Name""")

    choice = input("Enter Which Data You Want to Update: ").strip()

    if choice == '1':
        pub_id = input("Enter the Correct Publisher ID ( 6-digit ): ").strip()
        sql = f"""update Library set
                    PubID = '{pub_id}'
                    where BookID = '{book_id}'"""
        cur.execute(sql)
        con.commit()
        print("\nData Updated Successfully!")

    elif choice == '2':
        book_name = input("Enter the Updated Book Name: ").title().strip()
        sql = f"""update Library set
                        Book_name = '{book_name}'
                        where BookID = '{book_id}'"""
        cur.execute(sql)
        con.commit()
        print("\nData Updated Successfully!")

    elif choice == '3':
        New_book_Id = input("Enter The Correct Book ID: ").strip()
        sql = f"""update Library
                        set BookID = '{New_book_Id}'
                        where BookID = '{book_id}'"""
        cur.execute(sql)
        con.commit()
        print("\nData Updated Successfully!")


    elif choice == '4':
        author = input("Enter the Updated Author name:  ").title().strip()
        sql = f"""update Library set
                        Author= '{author}'
                        where BookID = '{book_id}'"""
        cur.execute(sql)
        con.commit()
        print("\nData Updated Successfully!")

    elif choice == '5':
        pub_name = input("Enter Updated Publisher Name: ").title().strip()
        sql = f"""update Library set
                         Pub_Name = '{pub_name}'
                        where BookID = '{book_id}'"""
        cur.execute(sql)
        con.commit()
        print("\nData Updated Successfully!")


    else:
        print(f"The choice is incorrect!")
        update_book()