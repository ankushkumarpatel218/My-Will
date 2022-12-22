import sqlite3
con = sqlite3.connect('Library.db')
cur = con.cursor()


def Remove_book():
    print("*********************\n"
          "Removing a Book Data-\n"
          "*********************")
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
        delete = f'delete from Library where BookID = "{book_id}"'
        cur.execute(delete)
        con.commit()
        print('\nThe Book Data Successfully Deleted!\n')
    else:
        print(f"\nBook With {book_id} this ID is not in the Library!\n")