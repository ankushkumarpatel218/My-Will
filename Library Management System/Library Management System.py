from Add_book import *
from Issue_book import *
from Return_book import *
from Remove_book import *
from updt_book import *
from Show_available_books import *
from Show_Pub_Books import *
from show_author_books import *
from Show_not_returned_book import *

def main():
    print('**************************************')
    print('1. Add a new book ')
    print('2. Issues a book')
    print('3. Return a book')
    print('4. Remove a book data ')
    print('5. update the book details')
    print('6. Show the available books')
    print('7. Show the all books published by particular publisher')
    print('8. Show the all books of Particular Author')
    print('9. Show the all Books Which are not Returned yet\n'
          '********************************************************')

    choice = input('\nEnter the option number:')

    if choice == '1':
        add_book()
        main()

    elif choice == '2':
        issue_book()
        main()
        #function2 - issue function

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
        #function5 - Update function

    elif choice == '6':
        show_avl_books()
        main()
        #function6 - show all Available Books


    elif choice == '7':
        show_pub_books()
        main()
        #function7 - Show the all books published by particular publisher

    elif choice == '8':
        show_aut_books()
        main()
        #function8 - Show the all books of Particular Author

    elif choice == '9':
        show_not_return_book()
        main()
        # function9 - Show the all Books Which are not Returned yet

if __name__ == "__main__":
    main()
