import sqlite3
con = sqlite3.connect('Library.db')
cur = con.cursor()

# cur.execute('''Create table Library
#                     (Acc_no varchar(5) primary key, Book_name varchar(30)) ''')



# cur.execute('''alter table library
#             add pubID varchar(5)''')



# cur.execute('delete from library where condition')
# con.commit()



# while True:
#     qry1 = input('enter acc no. ')
#     qry2 = input('enter Book name:')
#     qry3 = input('enter Publisher_name')
#     qry4 = input('enter pubID')
#     cur.execute(f'''insert into library
#                 values("{qry1}","{qry2}","{qry3}", "{qry4}")''')
#     con.commit()
#     if input('wanna quit? ') == '*':
#         break
#
#     else:
#         continue
