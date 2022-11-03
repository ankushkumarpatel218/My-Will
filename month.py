months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
user = input("input the month: ").title()

if user in months:
    if user in ['January', 'March', 'May', 'July', 'August', 'October', 'December']:
        print(f"\nlist of the months: {months}")
        print(f"\nthe input month: {user}")
        print(f"\nnumber of days in {user}: 31 days")

    elif user in ['April', 'June', 'September', 'November']:
        print(f"\nlist of the months: {months}")
        print(f"\nthe input month: {user}")
        print(f"\nnumber of days in {user}: 30 days")

    else:
        print(f"\nlist of the months: {months}")
        print(f"\nthe input month: {user}")
        print(f"\nnumber of days in {user}: 28/29 days")

else:
    print("Please enter right month!")