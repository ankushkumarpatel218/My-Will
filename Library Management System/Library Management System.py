from Add_book import *
from Issue_book import *

def return_book():
    bookid = input('Enter Book Id number: ')

def main():
    print('\n1. Add a new book ')
    print('2. issues a book')
    print('3. return a book')
    print('4. Remove a book data ')
    print('5. update the book details')
    print('6. Show the available books')
    print('7. Show the books published by particular publisher')
    print('8. Show the books of Particular Author')

    choice = input('\nEnter the option number:')

    if choice == '1':
        add_book()
        main()

    elif choice == '2':
        issue_book()
        main()
        #function2 - issue function

    elif choice == '3':
        pass
        main()
        # function3 - remove function

    elif choice == '4':
        pass
        main()
        # function4 - update function

    elif choice == '5':
        pass
        main()
        #function5 - show particular data , show function


if __name__ == "__main__":
    main()
