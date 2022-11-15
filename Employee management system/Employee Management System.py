# Employee Management System

from Add_Employee import *
from Remove_Employee import *
from Update_Employee import *
from Promote_Employee import *
from Search_Employee import *
from Emp_com_dept import *
from Emp_com_role import *


def main():
    print('******************************************')
    print("1.Add Employee Data\n"
          "2.Remove Employee Data\n"
          "3.Update Employee Data\n"
          "4.Promotion of an Employee\n"
          "5.Search for an Employee Data\n"
          "6.Show Employee with common department\n"
          "7.Search for Employee with common role\n"
          '*******************************************')

    choice = input('\nEnter the option number:')

    if choice == '1':
        add_emp()
        main()
        # function1 - Add Employee Data function

    elif choice == '2':
        remove_emp()
        main()
        # function2 - Remove Employee Data function

    elif choice == '3':
        update_emp()
        main()
        # function3 - Update Employee Data function

    elif choice == '4':
        promote_emp()
        main()
        # function4 - Promotion of an Employee function

    elif choice == '5':
        search_emp()
        main()
        # function5 - Search for an Employee Data function

    elif choice == '6':
        com_dept_emp()
        main()
        # function6 - Show Employee with common department Rooms

    elif choice == '7':
        com_role_emp()
        main()
        # function7 - Search for Employee with common role

    else:
        print("Wrong Option! Pls try Again")
        main()


if __name__ == "__main__":
    main()
