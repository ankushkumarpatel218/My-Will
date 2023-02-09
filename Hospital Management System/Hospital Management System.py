# Hospital Management System

from Add_bed import *
from Remove_bed import *
from Hospitalize import *
from Discharge import *
from Show_Register import *
from Show_all_Available_beds import *
from Show_type_Room import *
from Search_for_Bed import *
from Show_Com_Disease import *


def main():
    print('******************************************')
    print("1.Add Bed in a Ward\n"
          "2.Remove Bed from a Ward\n"
          "3.Hospitalize a Patient\n"
          "4.Discharge a Patient\n"
          "5.Show Hospital Register\n"
          "6.Show all Available Bed\n"
          "7.Search for Particular type of Bed Room\n"
          "8.Search for Particular Bed\n"
          "9.Search for Patient With Common Disease\n"
          '*******************************************')

    choice = input('\nEnter the option number:').strip()

    if choice == '1':
        add_bed()
        main()

    elif choice == '2':
        remove_bed()
        main()

    elif choice == '3':
        hospitalize()
        main()

    elif choice == '4':
        discharge()
        main()

    elif choice == '5':
        show_register()
        main()

    elif choice == '6':
        show_alv_bed()
        main()

    elif choice == '7':
        search_type_room()
        main()

    elif choice == '8':
        search_bed()
        main()

    elif choice == '9':
        show_com_disease()
        main()
        
    else:
        print("Wrong Option! Pls try Again")
        main()


if __name__ == "__main__":
    main()
    