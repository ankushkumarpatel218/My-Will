from Add_student import *
from Show_stu import *
from Update_stu import *
from Delete_stu import *
from Show_num_stu import *
from show_num_male_female_stu import *
from Show_all_student import *


def main():
    print(""" ***********************************************************
 1.Add New Student Data                                     |
 2.Display Particular Student Data                          |
 3.Update Particular Student Data                           |
 4.Delete Particular Student Data                           |
 5.Show all student in particular class                     | 
 6.Show all Male/Female student in particular Class         | 
 7.Show all students data                               |
 ************************************************************\n""")
    choice = input("Enter Task No:")
    while True:
        if choice == '1':
            add_stu()
            main()

        elif choice == '2':
            show_stu()
            main()

        elif choice == '3':
            update_stu()
            main()

        elif choice == '4':
            del_stu()
            main()

        elif choice == '5':
            show_num_stu()
            main()

        elif choice == '6':
            show_num_male_female_stu()
            main()

        elif choice == '7':
            show_all_stu()
            main()

        else:
            print("wrong choice...\npls try again!")
            break


if __name__ == "__main__":
    main()