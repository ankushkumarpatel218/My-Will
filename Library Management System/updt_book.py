import sqlite3
con = sqlite3.connect('Library.db')
cur = con.cursor()


def update_book():
    print("*******************\n"
          "Updating Book Data-\n"
          "*******************")
    book_id = input('Enter Book ID ( 4-digit ): ')
    print("""    1.Accession number
    2.Book name
    3.BookID
    4.Author
    5.Publisher Name
    6.Publisher ID""")

    choice = input("Enter Which Data You Want to Update: ")

    if choice == '1':
        Acc_no = input("Enter the Correct accession number: ")
        sql = f"""update Library set
                values Accession_no = '{Acc_no}'
                where BookID = '{book_id}'"""
        cur.execute(sql)
        con.commit()
        print("\nData Updated Successfully!")

    elif choice == '2':
        book_name = input("Enter the Updated Book Name: ")
        sql = f"""update Library set
                        values Book_name = '{book_name}'
                        where BookID = '{book_id}'"""
        cur.execute(sql)
        con.commit()
        print("\nData Updated Successfully!")

    elif choice == '3':
        New_book_Id = input("Enter The Correct Book ID: ")
        sql = f"""update Library set
                        values BookID = '{New_book_Id}'
                        where BookID = '{book_id}'"""
        cur.execute(sql)
        con.commit()
        print("\nData Updated Successfully!")


    elif choice == '4':
        author = input("Enter the Updated Author name:  ")
        sql = f"""update Library set
                        values Author= '{author}'
                        where BookID = '{book_id}'"""
        cur.execute(sql)
        con.commit()
        print("\nData Updated Successfully!")

    elif choice == '5':
        pub_name = input("Enter Updated Publisher Name: ")
        sql = f"""update Library set
                        values Pub_Name = '{pub_name}'
                        where BookID = '{book_id}'"""
        cur.execute(sql)
        con.commit()
        print("\nData Updated Successfully!")

    elif choice == '6':
        pub_id = input("Enter the Correct Publisher ID ( 6-digit ): ")
        sql = f"""update Library set
                        values PubID = '{pub_id}'
                        where BookID = '{book_id}'"""
        cur.execute(sql)
        con.commit()
        print("\nData Updated Successfully!")

    else:
        print(f"The choice is incorrect!")
        update_book()