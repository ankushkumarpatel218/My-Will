# Library Management System

from Add_book import *
from Issue_book import *
from Return_book import *
from Remove_book import *
from updt_book import *
from Show_available_books import *
from Show_Pub_Books import *
from show_author_books import *
from Show_not_returned_book import *
from Show_Register import *
from Search_for_book import *


def main():
    print("""\n************************\n
          Library Management System
          \n***************************\n""")
    
    print('******************************************')
    print('1. Add a new book ')
    print('2. Issues a book')
    print('3. Return a book')
    print('4. Remove a book data ')
    print('5. update the book details')
    print('6. Show the available books')
    print('7. Show the all books published by particular publisher')
    print('8. Show the all books of Particular Author')
    print("9. Show the all Books Which haven't Returned yet\n"
          "10. Show the Register\n"
          "11. Search for a particular Book\n"
          '********************************************************')

    choice = input('\nEnter the option number:')

    if choice == '1':
        add_book()
        main()
        # function1 - Add book function

    elif choice == '2':
        issue_book()
        main()
        # function2 - issue function

    elif choice == '3':
        return_book()
        main()
        # function3 - return function

    elif choice == '4':
        Remove_book()
        main()
        # function4 - remove function

    elif choice == '5':
        update_book()
        main()
        # function5 - Update function

    elif choice == '6':
        show_avl_books()
        main()
        # function6 - show all Available Books

    elif choice == '7':
        show_pub_books()
        main()
        # function7 - Show the all books published by particular publisher

    elif choice == '8':
        show_aut_books()
        main()
        # function8 - Show the all books of Particular Author

    elif choice == '9':
        show_not_return_book()
        main()
        # function9 - Show the all Books Which are not Returned yet

    elif choice == '10':
        show_register()
        main()
        # Show the Register

    elif choice == '11':
        search_book()
        main()
        # Search for a particular Book

    else:
        print("Wrong Option! Pls try Again")
        main()


def library():
    print("*********************************\n"
          "Enter Your Password Library Admin: -\n"
          "*********************************")
    password = input(">>> ").strip()
    with open("Library Admin Password.txt", "r") as admin:
        read1 = admin.read()
        if password == read1:
            main()
        else:
            print("\nWrong Password! Pls Try again\n")
            library()


if __name__ == "__main__":
    library()




