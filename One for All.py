import datetime
now = datetime.datetime.now()
check_out_date = now.strftime(f"%d/%m/{20}%y %H:%M:%S")
print(check_out_date)