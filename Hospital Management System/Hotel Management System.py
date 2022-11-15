# Hotel Management System

from Add_room import *
from Remove_room import *
from Check_in import *
from Check_out import *
from Show_Register import *
from Show_all_Available_room import *
from Show_type_Room import *
from Search_for_Room import *


def main():
    print('******************************************')
    print("1.Add Room Data\n"
          "2.Remove Room Data\n"
          "3.Check In\n"
          "4.Check Out\n"
          "5.Show Register\n"
          "6.Show all Available Rooms\n"
          "7.Search for Particular type of Room\n"
          "8.Search For Particular Room\n"
          '*******************************************')

    choice = input('\nEnter the option number:').strip()

    if choice == '1':
        add_room()
        main()
        # function1 - Add Room function

    elif choice == '2':
        remove_room()
        main()
        # function2 - Remove Room function

    elif choice == '3':
        check_in()
        main()
        # function3 - Check In function

    elif choice == '4':
        check_out()
        main()
        # function4 - Check Out function

    elif choice == '5':
        show_register()
        main()
        # function5 - Show Register function

    elif choice == '6':
        show_alv_room()
        main()
        # function6 - Show All Available Rooms

    elif choice == '7':
        search_type_room()
        main()
        # function7 - Search for Particular Type Room

    elif choice == '8':
        search_room()
        main()
        # function8 - Search for Particular Room

    else:
        print("Wrong Option! Pls try Again")
        main()


if __name__ == "__main__":
    main()